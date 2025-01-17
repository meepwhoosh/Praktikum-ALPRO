import random

def cek_pilihan_pengguna ():
    pilihan = ['gunting', 'batu', 'kertas']
    pilihan_pengguna = str(input("pilih pilihan anda : gunting, batu, atau kertas? ")).lower()

    while pilihan_pengguna not in pilihan :
        print("Pilihan anda tidak benar. pilihlah sesuai aturan")
        pilihan_pengguna = str(input("pilih pilihan anda : gunting, batu, atau kertas? ")).lower()

    return pilihan_pengguna

def cek_pilihan_komputer():
    pilihan = ["gunting", "batu", "kertas"]
    pilihan_komputer = random.choice(pilihan)
    
    return pilihan_komputer

def memilih_pemenang(pilihan_pengguna, pilihan_komputer):
    print(f"komputer memilih : {pilihan_komputer}")

    if pilihan_pengguna == pilihan_komputer :
        return "Seimbang"
    elif (
        (pilihan_pengguna == 'gunting' and pilihan_komputer == 'kertas') or
        (pilihan_pengguna == 'batu' and pilihan_komputer == 'gunting') or
        (pilihan_pengguna == 'kertas' and pilihan_komputer == 'batu')
    ):
        return "anda menang, komputer kalah"
    else :
        return "komputer menang, anda kalah"

def game():
    pilihan_pengguna = cek_pilihan_pengguna()
    pilihan_komputer = cek_pilihan_komputer()
    hasil = memilih_pemenang(pilihan_pengguna, pilihan_komputer)
    print(hasil)

    bermain_lagi = input("apakah kamu ingin bermain lagi? ya/tidak ").lower()
    if bermain_lagi == 'ya':
        game()
    else :
        print('terima kasih telah bermain')

print('--- selamat datang di permainan suit ---', '\n')
game()

