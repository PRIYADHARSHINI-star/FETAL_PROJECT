from django.shortcuts import render
from django.http import HttpResponse
from authentication.models import Register, contact1,User_Detail
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import joblib

# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pswrd = request.POST['pswrd']
        confirm = request.POST['confirm']
        if pswrd==confirm:
            salt = "5gz"
            dataBase_password = pswrd+salt
            hashed = hashlib.md5(dataBase_password.encode())
            crypted_pass= hashed.hexdigest()
            ins1 = Register(Username=username, First_Name = fname, Last_Name = lname, Email = email, Password = crypted_pass, Confirm_Password = crypted_pass)
            ins1.save()
            print("Data saved to db")
        else:
            print("Enter password properly")
    return render(request, 'authentication/register.html')

def login(request):
    if request.method=="POST":
        Email_id = request.POST['Email_id']
        pswrd = request.POST['pswrd']
        salt="5gz"
        pass1 = pswrd+salt
        hashed1 = hashlib.md5(pass1.encode())
        decrypt_pass = hashed1.hexdigest()
        register_user = Register.objects.filter(Email=Email_id, Password=decrypt_pass)
        if register_user:
            return render(request,'authentication/predict.html')
        else:
            print("Not registered")
    return render(request, 'authentication/login.html')

def contacting(request):
    if request.method=="POST":
        beg_name = request.POST["fname"]
        end_name = request.POST["lname"]
        cont_num = request.POST["phone_nu"]
        em_id = request.POST["mail_id"]
        messages = request.POST["w3review"]
        cont = contact1(first_name=beg_name,last_name=end_name,contact_number=cont_num,email_id=em_id,Messages=messages)
        cont.save()
        print("Data Saved to database")
    return render(request,"authentication/contacting.html")

def about(request):
    return render(request,"authentication/about.html")

def predict(request):
    return render(request, 'authentication/predict.html')

#def generate_iv():
#    return get_random_bytes(AES.block_size)

#def encrypt_data(data, key):
#    iv = generate_iv()
#    cipher = AES.new(key, AES.MODE_CBC, iv)
#    padded_data = pad(data.encode('utf-8'), AES.block_size)
#    encrypted_data = cipher.encrypt(padded_data)
#    return iv + encrypted_data

#def decrypt_data(encrypted_data, key):
#    iv = encrypted_data[:AES.block_size]
#    cipher = AES.new(key, AES.MODE_CBC, iv)
#    decrypted_data = cipher.decrypt(encrypted_data[AES.block_size:])
#    unpadded_data = unpad(decrypted_data, AES.block_size)
#    return unpadded_data.decode('utf-8')

def encrypt_data(message, key):
    message = message.encode()
    padding = 16 - (len(message) % 16)
    message += bytes([padding] * padding)
    key = key[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def decrypt_data(ciphertext, key):
    key = key[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.decrypt(ciphertext)
    padding = message[-1]
    message = message[:-padding]
    message = message.decode()
    return message

def results(request):
    cls = joblib.load('authentication/Final_Random_encrypted_Model.sav')

    Patient_ID = request.GET.get('Patient_ID')
    Abs_var= request.GET.get('Abs_var')
    Pec_abl = request.GET.get('Pec_abl')
    me_st = request.GET.get('me_st')
    His_mean = request.GET.get('His_mean')
    Pro_dec= request.GET.get('Pro_dec')
    His_med = request.GET.get('His_med')
    Acc = request.GET.get('Acc')
    His_mod = request.GET.get('His_mod')
    Me_lt = request.GET.get('Me_lt')
    His_min = request.GET.get('His_min')

    key = "the key is somerandombullshit"

    print(Abs_var)  
    # Encrypt each input value separately
    encrypted_patient = encrypt_data(str(Patient_ID),key)
    encrypted_abs = encrypt_data(str(Abs_var), key)
    encrypted_pec = encrypt_data(str(Pec_abl), key)
    encrypted_me = encrypt_data(str(me_st),key)
    encrypted_his = encrypt_data(str(His_mean), key)
    encrypted_pro = encrypt_data(str(Pro_dec), key)
    encrypted_med = encrypt_data(str(His_med), key)
    encrypted_acc = encrypt_data(str(Acc),key)
    encrypted_hismod = encrypt_data(str(His_mod), key)
    encrypted_lt = encrypt_data(str(Me_lt),key)
    encrypted_hismin = encrypt_data(str(His_min), key)

    patient = User_Detail(Patient_ID = encrypted_patient,Abnormal_short_term_variability=encrypted_abs,Percentage_of_time_with_ALTV=encrypted_pec,Mean_value_short_term=encrypted_me,
                        Histogram_mean=encrypted_his,Prolongued_decelerations=encrypted_pro,Histogram_median=encrypted_med,
                        Accelerations=encrypted_acc,Histogram_mode=encrypted_hismod,Mean_value_of_LTV=encrypted_lt,
                        Histogram_min=encrypted_hismin)
    patient.save()

    decrypted_abs = decrypt_data(encrypted_abs, key)
    decrypted_pec = decrypt_data(encrypted_pec, key)
    decrypted_me = decrypt_data(encrypted_me ,key)
    decrypted_his = decrypt_data(encrypted_his, key)
    decrypted_pro = decrypt_data(encrypted_pro, key)
    decrypted_med = decrypt_data(encrypted_med, key)
    decrypted_acc = decrypt_data(encrypted_acc ,key)
    decrypted_hismod = decrypt_data(encrypted_hismod, key)
    decrypted_lt = decrypt_data(encrypted_lt ,key)
    decrypted_hismin = decrypt_data(encrypted_hismin, key)

    lis=[encrypted_abs,encrypted_pec,encrypted_me,encrypted_his,encrypted_pro,encrypted_med,encrypted_acc,encrypted_hismod,encrypted_lt,encrypted_hismin]
    for i in range(len(lis)):
        lis[i]=int.from_bytes(lis[i], byteorder='big')
        lis[i]=float(lis[i])

    predictions = cls.predict([lis])
    print(lis)
    if predictions[0]== 1:
        predictions = "Normal"
    elif predictions[0]==2:
        predictions = "Suspect"
    elif predictions[0] == 3:
        predictions = "Pathological"
    else:
        pass
        
    print("Predicted value",predictions)

    return render(request, 'authentication/predict.html',{'result':predictions})