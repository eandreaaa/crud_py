import mysql.connector

koneksi = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "db_python"
)

mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1. Lihat User")
    print("2. Tambah User")
    print("3. Ubah User")
    print("4. Hapus User")
    print("5. Keluar")
    print("")

    p = int(input("Pilih Menu :"))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("======================")
        print("(id,nama,email,no hp)")
        for x in myresult:
            print(x)
    elif(p == 2):
        nama = input("Nama :")
        email = input("Email :")
        no_hp = input("No HP :")
        sql = "INSER INTO user (nama, email, no_hp) VALUES (%s, %s, %s)"
        val = (nama, email, no_hp)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data user berhasil ditambah")
    elif(p == 3):
        id = input("ID USER : ")
        