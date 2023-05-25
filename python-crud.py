import mysql.connector

koneksi = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "crud_python"
)

mycursor = koneksi.cursor()

lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD Data")
    print("1. Lihat Data")
    print("2. Tambah Pengguna")
    print("3. Ubah Data")
    print("4. Hapus")
    print("5. Keluar")
    print("")
    
    p = int(input("Pilih menu : "))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("======================")
        # print("(id,nama,no_hp,umur)")
        for x in myresult:
            print(x)
    elif(p == 2):
        nama = input("NAMA :")
        no_hp = input("NO HP :")
        umur = input("UMUR :")
        sql = "INSERT INTO user (nama, no_hp, umur) VALUES (%s, %s, %s)"
        val = (nama, no_hp,umur)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "Data berhasil ditambah")
    elif(p == 3):
        id = input("ID Pengguna :")
        mycursor.execute("SELECT * FROM user where id="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
            
        if(user != None):
            nama = input("NAMA ("+user[1]+") :") or user[1]
            no_hp = input("NO HP ("+user[2]+") :") or user[2]
            umur = input("UMUR ("+user[3]+") :") or user[3]
            sql = "UPDATE user SET nama=%s,no_hp=%s,umur=%s WHERE id=%s"
            val = (nama, no_hp,umur,id)
            koneksi.commit()
            print(mycursor.rowcount, "Data berhasil disimpan")
        else:
            print("Data tidak ditemukan")
    elif(p == 4):
        id = input("ID Pengguna :")
        mycursor.execute("SELECT * FROM user where id="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("Menghapus Data Pengguna :",user)
            sql = "DELETE FROM user WHERE id"+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "Data berhasil di hapus")
        else:
            print("Data tidak ditemukan")
    elif(p == 5):
        lanjut = False
        