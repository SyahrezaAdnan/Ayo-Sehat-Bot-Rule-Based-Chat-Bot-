import re
import random
class Rule_Bot:

  def __init__(self):

    # Fitur 1 menurunkan berat badan keywords
    self.f_1_commands = ("nurunin", "menurunkan", "diet", "turun", "turunin", "nurun", "turun", "mengurangi", "ngurusin", "kurusin", "mengkuruskan", "kurang", "ngurangi")

    # Fitur 1.1 aktivitas yang membakar kalori keywords
    self.f_1_1_commands= ("aktivitas", "bakar", "bakar kalori", "membakar", "membakar kalori", "ngebakar", "ngebakar kalori", "aktivitas yang membakar kalori", "kalori terbakar", "gerak")

    # Fitur 1.2 rekomendasi makanan diet keywords
    self.f_1_2_commands = ("makanan", "diet", "makanan diet", "makanan penurun berat badan", "makanan untuk diet", "makanan yang bisa nurunin berat badan",
                           "makanan yang menurunkan berat badan", "makanan untuk orang diet", "rekomendasi makanan diet", "makan")

    # Fitur 1.3 perhitungan pembakaran kalori keywords
    self.f_1_3_commands = ("perhitungan", "hitung", "perhitungan pembakaran kalori", "itung", "waktu")

    # Fitur 1.1 list aktivitas
    self.f_1_1_list = (
        "Berkebun dapat membakar 440 kalori setiap 1 jam",
        "Mendaki gunung dapat membakar 370 kalori setiam 1 jam",
        "Berenang dapat membakar 510 kalori setiap 1 jam",
        "Bersepeda dapat membakar 288 hingga 594 kalori setiap 30 menit",
        "Berjalan atau berlari dapat membakar 120 hingga 480 kalori setiap 30 menit",
        "Lompat tali dapat membakar 495 kalori setiap 30 menit",
        "Panjat tebing dapat membakar 773 kalori setiap 1 jam",
        "Senam aerobik dapat membakar 396 hingga 588 kalori setiap 1 jam",
        "Senam yoga dapat membakar 228 hingga 364 kalori setiap 1 jam",
        "Permainan bola voli dapat membakar 364 kalori setiap 1 jam",
        "Permainan bola basket dapat membakar 728 kalori setiap 1 jam"
        )

    # Fitur 1.2 list makanan
    self.f_1_2_list = (
        # 1
        "Sarapan (324 kalori)\n"
        "1 porsi smoothie bayam, selai kacang, dan pisang\n\n"
        "Makan siang (393 kalori)\n"
        "1 porsi sup ayam dan kale\n"
        "1 pisang ukuran sedang \n\n"
        "Makan malam (466 kalori)\n"
        "1 porsi salad yunani dengan edamame\n"
        "1 apel sedang\n\n"
        "Camilan pagi (77 kalori)\n"
        "1 jeruk sedang\n\n"
        "Camilan sore (350 kalori)\n"
        "1 apel besar\n"
        "2 sendok makan selai kacang",

        # 2
        "Sarapan(271 kalori)\n"
        "1 porsi roti panggang dengan alpukat dan telur\n\n"
        "Makan siang(381 kalori)\n"
        "1 porsi mangkok gandum superfood vegan\n\n"
        "Makan malam(416 kalori)\n"
        "1 porsi kari kentang manis dan sup kacang\n"
        "1 iris roti gandum yang dipanggang\n\n"
        "Camilan pagi(95 kalori)\n"
        "1 apel sedang\n\n"
        "Camilan sore(84 kalori)\n"
        "1 cangkir blueberry",

        # 3
        "Sarapan(324 kalori)\n"
        "1 porsi smoothie bayam, selai kacang, dan pisang\n\n"
        "Makan siang(366 kalori)\n"
        "1 porsi tuna, kacang putih, dan salah adas\n"
        "1 iris roti gandum yang dipanggang\n\n"
        "Makan malam(304 kalori)\n"
        "1 porsi nasi dengan ayam goreng dan kembang kol\n\n"
        "Camilan pagi(214 kalori)\n"
        "1/4 cangkir almond panggang kering tanpa garam\n\n"
        "Camilan sore(77 kalori)\n"
        "1 jeruk sedang",

        # 4
        "Sarapan(491 kalori)\n"
        "1 cangkir yogurt Yunani polos rendah lemak\n"
        "1/4 cangkir raspberry\n"
        "3 sendok makan kenari cincang\n\n"
        "Makan siang(381 kalori)\n"
        "1 porsi mangkok gandum superfood vegan\n\n"
        "Makan malam(429 kalori)\n"
        "1 mangkuk udang panggang, pesto dan quinoa"
        "Camilan pagi(324 kalori)\n"
        "1 apel sedang\n"
        "2 sendok makan selai kacang\n\n"
        "Camilan sore(152 kalori)\n"
        "1/3 cangkir mentimun yang diris\n"
        "1/4 cangkir hummus",

        # 5
        "Sarapan(324 kalori)\n"
        "1 porsi smoothie bayam, selai kacang, dan pisang\n\n"
        "Makan siang(381 kalori)\n"
        "1 porsi mangkok gandum superfood vegan\n\n"
        "Makan malam(427 kalori)\n"
        "1 porsi ikan cod dengan saus krim tomat\n"
        "3/4 cangkir nasi merah\n"
        "1 cangkir brokoli kukus\n\n"
        "Camilan pagi(102 kalori)\n"
        "1 paprika sedang yang diiris\n"
        "3 sendok makan hummus\n\n"
        "Camilan sore(84 kalori)\n"
        "1 cangkir blueberry",

        # 6
        "Sarapan(355 kalori)\n"
        "1 porsi roti panggang dengan alpukat dan telur\n"
        "1 cangkir blueberry\n\n"
        "Makan siang(366 kalori)\n"
        "1 porsi tuna, kacang putih, dan salah adas\n"
        "1 iris roti gandum yang dipanggang\n\n"
        "Makan malam(304 kalori)\n"
        "1 porsi nasi dengan ayam goreng dan kembang kol\n\n"
        "Camilan pagi(62 kalori)\n"
        "1 jeruk sedang\n\n"
        "Camilan sore(95 kalori)\n"
        "1 apel sedang",

        # 7
        "Sarapan(324 kalori)\n"
        "1 porsi smoothie bayam, selai kacang, dan pisang\n\n"
        "Makan siang(393 kalori)\n"
        "1 porsi sup ayam dan kale\n"
        "1 pisang sedang\n\n"
        "Makan malam(466 kalori)\n"
        "1 porsi salad yunani dengan edamame\n"
        "1 apel sedang\n\n"
        "Camilan pagi(214 kalori)\n"
        "1/4 cangkir almond panggang kering tanpa garam\n\n"
        "Camilan sore(183 kalori)\n"
        "1 paprika sedang\n"
        "1/4 cangkir hummus"
        )

    # Fitur 2 menaikkan berat badan keywords
    self.f_2_commands = ("naikkin", "naikin", "menaikkan", "menaikan", "naik", "menambahkan", "gemukkin", "gemukin", "menggemukkan", "menggemukan", "tambah", "nambah")

    # Fitur 2.1 rekomendasi makanan yang menaikkan berat badan keywords
    self.f_2_1_commands = ("makanan", "rekomendasi makanan yang menaikkan berat badan", "makanan yang gemukkin", "makanan yang menggemukkan",
                           "makanan buat naikin berat badan", "makanan yang bikin gemuk", "makan")

    # Fitur 2.2 rekomendasi olahraga yang menambah massa otot keywords
    self.f_2_2_commands = ("olahraga", "otot", "rekomendasi olahraga yang menambah massa otot", "olahraga yang nambahin massa otot", "olahraga penambah massa otot")

    # Fitur 2.3 perhitungan waktu menaikkan berat badan keywords
    self.f_2_3_commands = ("perhitungan penambahan kalori", "perhitungan", "hitung", "waktu", "itung")

    # Fitur 2.1 list makanan
    self.f_2_1_list = (
        # 1
        "Sarapan (821 kalori)\n"
        "1 1/2 cangkir (120 gram) oat\n"
        "1 cangkir (240 ml) susu murni, diminum dengan oat\n"
        "3 telur utuh diaduk dengan 1 cangkir bayam\n\n"
        "Makan siang (864 kalori)\n"
        "Hamburger panggang dengan roti gandum dengan topping pilihan\n"
        "Ubi ukuran sedang untuk kentang goreng buatan sendiri\n"
        "2 sendok makan (14 gram) minyak zaitun dituang di atas kentang goreng\n\n"
        "Makan malam (861 kalori)\n"
        "Brokoli ayam alfredo\n\n"
        "Camilan pagi (294 kalori)\n"
        "1 buah apel utuh\n"
        "2 sendok makan (33 gram) selai kacang\n\n"
        "Camilan sore (291 kalori)\n"
        "1 buah pisang berukuran sedang\n"
        "Segenggam (1 ons) kacang kenari",

        # 2
        "Sarapan (669 kalori)\n"
        "2 potong roti gandum\n"
        "2 sendok makan (33 gram) selai kacang dioleskan di atas roti bakar\n"
        "2 sendok makan (41 gram) madu dioleskan di atas roti panggang\n"
        "1 cangkir susu\n\n"
        "Makan siang (861 kalori)\n"
        "Brokoli ayam alfredo\n\n"
        "Makan malam (707 kalori)\n"
        "Salmon panggang dengan kentang merah dan kacang hijau\n\n"
        "Camilan pagi (500 kalori)\n"
        "1 cangkir (227 gram) yogurt Yunani susu murni\n"
        "1/2 cangkir (55 gram) granola untuk taburan\n\n"
        "Camilan sore (240 kalori)\n"
        "1 buah alpukat",

        # 3
        "Sarapan (880 kalori)\n"
        "Protein-oat\n\n"
        "Makan siang (707 kalori)\n"
        "Salmon panggang dengan kentang merah dan kacang hijau\n\n"
        "Makan malam (808 kalori)\n"
        "1 mangkuk burrito\n\n"
        "Camilan pagi (140 kalori)\n"
        "1 cangkir (140 gram) potongan mangga\n\n"
        "Camilan sore (240 kalori)\n"
        "1 buah alpukat",

        # 4
        "Sarapan (630 kalori)\n"
        "Susu kocok dengan pisang, oat, coklat, dan selai kacang\n\n"
        "Makan siang (808 kalori)\n"
        "1 mangkuk burrito\n\n"
        "Makan malam (918 kalori)\n"
        "Taco daging giling\n\n"
        "Camilan pagi (400 kalori)\n"
        "2 iris roti gandum\n"
        "1 cangkir keju cottage penuh lemak dioleskan di atas roti panggang\n"
        "irisan mentimun dan tomat untuk topping (opsional)\n\n"
        "Camilan sore (294 kalori)\n"
        "1 buah apel utuh\n"
        "2 sendok makan (33 gram) selai kacang",

        # 5
        "Sarapan (806 kalori)\n"
        "Sandwich selai kacang, pisang, dan madu\n\n"
        "Makan siang (901 kalori)\n"
        "Kentang panggang dengan tuna dan jagung manis\n\n"
        "Makan malam (881  kalori)\n"
        "1 mangkuk kentang tumbuk dengan ayam panggang\n\n"
        "Camilan pagi (294 kalori)\n"
        "1 buah apel utuh\n"
        "2 sendok makan (33 gram) selai kacang\n\n"
        "Camilan sore (119 kalori)\n"
        "1 granola bar",

        # 6
        "Sarapan (843 kalori)\n"
        "Oatmeal dengan pisang, madu, dan Kacang\n\n"
        "Makan siang (1000 kalori)\n"
        "Salmon dan salad pitta\n\n"
        "Makan malam (599 kalori)\n"
        "Fillet ikan cod besar (150g)\n"
        "300g potato wedges, dimasak dengan 1 sdm minyak\n"
        "Daun salad dicampur, 1 sdm minyak zaitun, dan bumbu\n\n"
        "Camilan pagi (119 kalori)\n"
        "1 granola bar\n\n"
        "Camilan sore (105 kalori)\n"
        "1 buah pisang sedang",

        # 7
        "Sarapan (802 kalori)\n"
        "50g granola, 30g oat, 150ml susu murni, dicampur\n"
        "25g kacang & 25g kismis\n"
        "Segelas jus jeruk\n\n"
        "Makan siang (858 kalori)\n"
        "Salad tuna dan kacang\n\n"
        "Makan malam (1279 kalori)\n"
        "Tumis ayam dan kacang mete\n\n"
        "Camilan pagi (380 kalori)\n"
        "30g kacang\n"
        "9 aprikot kering\n\n"
        "Camilan sore (280 kalori)\n"
        "40g Oat, 200ml Susu Murni, 1 sdt Madu, dicampur"
    )

    # Fitur 2.2 list olahraga
    self.f_2_2_list = (
        "Push up 5 set (1 set terdiri dari 15 sampai 20 kali push up)",
        "Deadlift",
        "Bench press",
        "Squats 4 set (satu set 8 kali repetisi) selama 45 menit",
        "Pull up repetisi sebanyak 10-15 kali",
        "Leg press",
        "Dips 8 repetisi sebanyak 3-4 set",
        "Mengangkat beban (dumbbell) 8 repetisi sebanyak 3-4 set",
    )

    # Fitur 3 motivasi keywords
    self.f_3_commands = ("dimotivasi", "motivasi", "motivasiin")

    # Fitur 3 motivasi
    self.f_3_motivation = (
        "Bukanlah tentang menjadi sempurna, tapi tentang menjadi sehat dan berusaha yang terbaik setiap hari.",
        "Setiap langkah kecil menuju kesehatan adalah investasi untuk masa depanmu yang lebih baik.",
        "Berat badan ideal adalah hasil dari pilihan sehat yang diambil setiap hari.",
        "Tubuh sehat adalah rumah bagi jiwa yang kuat dan bersemangat.",
        "Jangan pernah meremehkan kekuatan perubahan kecil. Mereka bisa menghasilkan perbedaan besar.",
        "Olahraga bukan hanya tentang mengubah tubuhmu, tapi juga tentang mengubah pikiranmu.",
        "Jika kamu berhenti sekarang, kamu hanya akan kembali ke titik awal. Teruslah maju, dan kamu akan mencapai tujuanmu.",
        "Berolahraga bukanlah pekerjaan, tapi investasi dalam kesehatan dan kebahagiaanmu sendiri.",
        "Makanlah untuk hidup, jangan hidup untuk makan.",
        "Asupan makanan yang baik adalah bahan bakar untuk tubuhmu. Pilihlah dengan bijaksana.",
        "Jangan menyerah pada keinginan sesaat dan jadikan visi jangka panjangmu sebagai prioritas.",
        "Tetap bergerak dan kamu akan merasakan energi yang tak terbatas.",
        "Setiap kali kamu memilih salad di atas makanan cepat saji, kamu memberi tubuhmu cinta dan perhatian yang sejati.",
        "Jaga badanmu seperti kamu menjaga harta berharga, karena kesehatan adalah harta yang tak ternilai.",
        "Menjaga keseimbangan antara aktivitas fisik dan pola makan yang baik adalah kunci untuk hidup sehat dan bahagia.",
        "Lakukan latihan hari ini, dan esok hari kamu akan berterima kasih padamu sendiri.",
        "Jika kamu ingin hasil yang berbeda, lakukan sesuatu yang berbeda.",
        "Berhenti mencari jalan pintas dan fokuslah pada perjalanan panjang menuju kesehatan optimal.",
        "Jadikan dirimu sebagai bukti bahwa perubahan gaya hidup bisa merubah segalanya.",
        "Kamu mungkin merasa lelah, tetapi ingatlah bahwa setiap langkah membawamu lebih dekat ke tujuanmu.",
        )

    # Penutup pembicaraan keywords
    self.exit_commands = ("goodbye", "dadah", "bye", "quit", "keluar", "sampai jumpa", "exit")

    # Pesan selamat tinggal
    self.exit_message = (
        "Sampai jumpa dan terima kasih sudah bersama AyoSehat-Bot. Jangan lupa, saya selalu ada di sini untukmu jika kamu membutuhkan bantuan atau tips seputar menjaga berat badan. "
        "Jadi, jika suatu saat kamu ingin tahu lebih banyak, ingatlah untuk kembali dan bertanya kepada saya. Tetap jaga kesehatan dan semangat! Sampai jumpa lagi!",
        "Sampai nanti, teman! Terima kasih telah menjadi bagian dari perbincangan dengan AyoSehat-Bot. "
        "Jika suatu hari nanti kamu butuh panduan tentang menjaga berat badan atau tips hidup sehat lainnya, jangan ragu untuk mencari saya. "
        "Tetaplah menjaga dirimu dan jangan lupa senyum setiap hari. Sampai jumpa, ya!",
        "Sampai jumpa, Sahabat Sehat! Waktunya kita berpisah sejenak. Jika muncul pertanyaan seputar pola makan sehat, olahraga, atau cara menjaga berat badan, "
        "jangan ragu untuk kembali dan berbicara dengan AyoSehat-Bot. Tetaplah bersemangat dalam menggapai tujuan hidup sehatmu. Selamat tinggal dan sampai bertemu lagi!",
        "Selamat tinggal untuk sementara! AyoSehat-Bot akan merindukan percakapan kita. "
        "Ingatlah, saya selalu siap membantu dengan informasi tentang gaya hidup sehat dan menjaga berat badan. "
        "Jangan ragu untuk kembali kapan pun kamu membutuhkan teman bicara yang penuh wawasan. Tetap sehat dan bahagia, ya! Sampai nanti!"
    )

    # Potensial negative respons
    self.negative_responses = ("no", "nope", "tidak", "ngga", "gak")



    # Pemberian daftar fitur
    self.list_of_fiture = (
        "Saat ini AyoSehat-Bot hanya memiliki 3 fitur utama\n"
        "1. Informasi menurunkan berat badan.\n"
        "2. Informasi menaikkan berat badan.\n"
        "3. Motivasi.\nApa yang anda butuhkan?")

    # Pemberian daftar fitur 1
    self.list_of_fiture_1 = (
        "Informasi yang dapat saya berikan mengenai menurunkan berat badan antara lain\n"
        "1. Rekomendasi aktivitas yang membakar kalori\n"
        "2. Rekomendasi makanan diet\n"
        "3. Perhitungan pembakaran kalori"
    )

    # Pemberian daftar fitur 2
    self.list_of_fiture_2 = (
        "Informasi yang dapat saya berikan mengenai menaikkan berat badan antar lain\n"
        "1. Rekomendasi makanan yang menaikkan berat badan\n"
        "2. Rekomendasi olahraga yang dapat membentuk massa otot\n"
        "3. Perhitungan penambahan kalori"
    )

    # Pencarian list fitur keywords
    self.list_of_fiture_commands = ("list", "daftar", "fitur", "fiture")


  def starter(self):
    print("Siapa namamu?")
    self.name = input()
    print(f"Halo {self.name}, saya adalah AyoSehat-Bot. Saya akan membantu menjaga berat badan mu\nApakah ada yang dapat saya bantu?")
    will_help = input().lower()
    if will_help in self.negative_responses:
      print("Oke. Tetapkan tujuan, tekad, dan berkomitmen untuk menjaga berat badan tubuh Anda dengan AyoSehat-Bot")
      return
    else:
      self.chat()

  def contain_commands(self, input_text, list_commands):
    for string in list_commands:
      if string in input_text:
        return True
    return False

  def chat(self):
    print(self.list_of_fiture)
    input_text = input().lower()
    while not self.contain_commands(input_text, self.exit_commands):
      if self.contain_commands(input_text, self.f_1_commands):
        self.fiture_1()
      elif self.contain_commands(input_text, self.f_2_commands):
        self.fiture_2()
      elif self.contain_commands(input_text, self.f_3_commands):
        self.fiture_3()
      elif self.contain_commands(input_text, self.list_of_fiture_commands):
        print(self.list_of_fiture)
      else:
        self.no_match_fiture()
      self.end_of_ask()
      input_text = input().lower()
    print(random.choice(self.exit_message))

  def fiture_1(self):
    print(self.list_of_fiture_1)
    input_text = input().lower()
    if self.contain_commands(input_text, self.f_1_3_commands):
      self.fiture_1_3()
    elif self.contain_commands(input_text, self.f_1_2_commands):
      self.fiture_1_2()
    elif self.contain_commands(input_text, self.f_1_1_commands):
      self.fiture_1_1()
    else:
      self.no_match_fiture()


  def fiture_1_1(self):
    print("Pada umumnya, untuk menurunkan berat badan 0,5-1 kg per minggu, kamu perlu mengurangi sekitar 500-1000 kalori per hari.")
    list_aktivitas = random.sample(self.f_1_1_list, 3)
    for item in list_aktivitas:
      print(item)

  def fiture_1_2(self):
    print("Pada umumnya, untuk menurunkan berat badan, kamu perlu mendapatkan asupan sekitar 1500 kalori saja tiap harinya")
    print(random.choice(self.f_1_2_list))

  def fiture_1_3(self):
    while True:
      print("Berapa berat badan mu saat ini?")
      input_text = input()
      bb_sekarang = self.get_int_from_str(input_text)
      while bb_sekarang == -1:
        print("Maaf, kamu harus mengetikkan berat badan mu yang saat ini")
        input_text = input()
        bb_sekarang = self.get_int_from_str(input_text)

      print("Lalu kamu ingin turun berat badan menjadi berapa?")
      input_text = input()
      bb_target = self.get_int_from_str(input_text)
      while bb_target == -1:
        print("Maaf, kamu harus mengetikkan target berat badanmu")
        input_text = input()
        bb_target = self.get_int_from_str(input_text)

      if bb_target >= bb_sekarang:
        print("Maaf, jika kamu ingin menurunkan berat badan, maka target berat badan mu harus lebih rendah dari pada berat badan mu saat ini")
      if bb_target < bb_sekarang:
        break

    waktu_tercepat = bb_sekarang - bb_target
    waktu_terlama =  waktu_tercepat * 2
    print(f"Jadi, jika kamu ingin menurunkan berat badan ke {bb_target} dari {bb_sekarang},\n")
    print(f"maka waktu tercepat untuk kamu menurunkan berat badan sekitar {waktu_tercepat} minggu, yaitu dengan membakar sekitar 1000 kalori tiap harinya.\n")
    print(f"Namun, jika kamu ingin menurunkan berat badan dengan lebih santai,\n")
    print(f"maka kamu dapat menurunkan berat badan dengan waktu sekitar {waktu_terlama} minggu, yaitu dengan membakar sekitar 500 kalori tiap harinya.")


  def fiture_2(self):
    print(self.list_of_fiture_2)
    input_text = input().lower()
    if self.contain_commands(input_text, self.f_2_3_commands):
      self.fiture_2_3()
    elif self.contain_commands(input_text, self.f_2_2_commands):
      self.fiture_2_2()
    elif self.contain_commands(input_text, self.f_2_1_commands):
      self.fiture_2_1()
    else:
      self.no_match_fiture()

  def fiture_2_1(self):
    print("Pada umumnya, untuk menaikkan berat badan, kamu perlu mendapatkan asupan sekitar 3000 kalori tiap harinya")
    print(random.choice(self.f_2_1_list))

  def fiture_2_2(self):
    print("Berikut merupakan contoh olahraga yang dapat menambah massa otot")
    list_olahraga = random.sample(self.f_2_2_list, 3)
    for item in list_olahraga:
      print(item)

  def fiture_2_3(self):
    while True:
      print("Berapa berat badan mu saat ini?")
      input_text = input()
      bb_sekarang = self.get_int_from_str(input_text)
      while bb_sekarang == -1:
        print("Maaf, kamu harus mengetikkan berat badan mu yang saat ini")
        input_text = input()
        bb_sekarang = self.get_int_from_str(input_text)

      print("Lalu kamu ingin turun berat badan menjadi berapa?")
      input_text = input()
      bb_target = self.get_int_from_str(input_text)
      while bb_target == -1:
        print("Maaf, kamu harus mengetikkan target berat badanmu")
        input_text = input()
        bb_target = self.get_int_from_str(input_text)

      if bb_target <= bb_sekarang:
        print("Maaf, jika kamu ingin menaikkan berat badan, maka target berat badan mu harus lebih tinggi dari pada berat badan mu saat ini")
      if bb_target > bb_sekarang:
        break

    waktu_tercepat = bb_sekarang - bb_target
    waktu_terlama =  round((waktu_tercepat*7) / 2 * 3)
    waktu_terlama_minggu = waktu_terlama // 7
    waktu_terlama_hari = waktu_terlama % 7
    print(f"Jadi, jika kamu ingin menaikkan berat badan ke {bb_target} dari {bb_sekarang},\n")
    print(f"maka waktu tercepat untuk kamu menaikkan berat badan sekitar {waktu_tercepat} minggu, yaitu dengan mendapatkan asupan sekitar 3000 kalori tiap harinya.\n")
    print(f"Namun, jika kamu ingin menaikkan berat badan dengan lebih santai,\n")
    print(f"maka kamu dapat menaikkan berat badan dengan waktu sekitar {waktu_terlama_minggu} minggu dan {waktu_terlama_hari} hari, yaitu dengan mendapatkan asupan sekitar 2000 kalori tiap harinya.")

  def fiture_3(self):
    print(random.choice(self.f_3_motivation))

  def no_match_fiture(self):
    print("Terima kasih sudah berbincang dengan AyoSehat-Bot.\n"
    "Maaf ya, sepertinya saya masih perlu belajar untuk merespons semua yang kamu katakan.\n"
    "Terima kasih atas kesabaran dan pengertiannya!")

  def end_of_ask(self):
    random_fiture = (
        "Cobalah fitur lain ku seperti informasi menurunkan berat badan",
        "Cobalah fitur lain ku seperti informasi menaikkan berat badan",
        "Cobalah fitur lain ku seperti motivasi")
    print("Apakah ada hal lain yang perlu saya bantu?")
    print(random.choice(random_fiture))

  def get_int_from_str(self, string):
    match = re.search(r'\d+', string)
    if match:
      angka_pertama = int(match.group())
      return angka_pertama
    else:
      return -1




AyoSehatBot = Rule_Bot()
AyoSehatBot.starter()