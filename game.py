import time

def main():
    print("Selamat datang di Game Pemecahan Misteri: Pembunuhan Misterius!")
    print("Anda adalah detektif yang harus menyelesaikan kasus pembunuhan.")
    nama = input("Masukkan nama Anda: ")
    print(f"\nHalo, Detektif {nama}! Mari kita mulai.")
    time.sleep(1)

    while True:
        print("\nPilih kasus yang ingin Anda selesaikan:")
        print("1. Misteri Pembunuhan Pengusaha Tua di Vila Kuno Jakarta - 2023")
        print("2. Misteri Racun di Kantor Teknologi Bandung - 2024")
        print("3. Misteri Tenggelam di Pesta Mewah Bali - 2025")
        pilihan = input("Masukkan nomor kasus (1-3): ")
        if pilihan == '1':
            case1(nama)
        elif pilihan == '2':
            case2(nama)
        elif pilihan == '3':
            case3(nama)
        else:
            print("Pilihan tidak valid. Coba lagi.")
            continue
        lagi = input("\nApakah Anda ingin memainkan kasus lain? (y/n): ")
        if lagi.lower() != 'y':
            break
    print(f"\nTerima kasih telah bermain, Detektif {nama}!")

def case1(nama):
    print("\n=== Misteri Pembunuhan Pengusaha Tua di Vila Kuno Jakarta - 2023 ===")
    print("Di malam yang hujan deras pada bulan Oktober 2023, vila kuno di pinggiran kota Jakarta menjadi saksi bisu tragedi mengerikan. Mr. Smith, seorang duda berusia 65 tahun yang dikenal sebagai pengusaha sukses namun misterius, ditemukan tewas di ruang tamu pukul 22:00. Ia menderita depresi kronis sejak istri meninggal dalam kecelakaan mobil 10 tahun lalu, masalah kesehatan mental yang sering diabaikan dalam masyarakat kita. Luka tusuk dalam di dada menunjukkan pembunuhan yang direncanakan dengan teliti, namun pintu vila terkunci dari dalam, membuat polisi bingung dan menduga bunuh diri. Tidak ada tanda perjuangan, seolah korban menerima takdirnya dengan tenang. Vila ini penuh dengan rahasia keluarga, termasuk tekanan finansial anaknya akibat pandemi yang menghantam ekonomi. Seperti dalam misteri Detective Conan, kasus ini melibatkan alibi palsu, clue tersembunyi, dan deduksi logis untuk mengungkap pelaku. Anda, Detektif, harus mengungkap misteri ini melalui wawancara dengan saksi-saksi yang mungkin menyimpan kunci kebenaran, sambil mempertimbangkan isu kesehatan mental dan dampak sosial. Setiap pilihan dialog Anda bisa mengubah jalannya penyelidikan.")
    print("Anda harus menemukan pelaku dengan berinteraksi dengan saksi.")
    time.sleep(2)

    clues = 0  # Track clues collected

    # Saksi 1: Tetangga
    print("\nAnda tiba di rumah tetangga yang tenang di sebelah rumah korban. Mrs. Johnson, seorang wanita paruh baya dengan rambut abu-abu, menyambut Anda dengan wajah khawatir dan mata merah karena kurang tidur.")
    print(f"Mrs. Johnson: 'Detektif {nama}, ini mengerikan sekali. Saya tinggal di sebelah selama 20 tahun, dan belum pernah terjadi hal seperti ini. Saya melihat seseorang masuk rumah Mr. Smith pukul 21:00, tapi saya tidak yakin siapa. Saya sedang menyiram tanaman di halaman, hujan deras membuat tanah basah. Orang itu berjalan cepat, seolah takut ketahuan.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang penampilan orang tersebut.")
    print("2. Tanya apakah ada suara aneh.")
    print("3. Tanya tentang hubungan dengan korban.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print(f"Mrs. Johnson: 'Orang itu tinggi, sekitar 180 cm, berpakaian gelap seperti jaket hitam yang basah kuyup karena hujan, dan berjalan cepat dengan kepala menunduk. Saya pikir itu pria, tapi dari jauh sulit dikatakan. Mungkin dia membawa sesuatu di tangan, seperti tas kecil. Saya tidak berani mendekat karena takut, Detektif {nama}.'")
        clues += 1
        print("Anda mencatat deskripsi tersebut. Ini bisa jadi clue penting untuk mengidentifikasi pelaku.")
    elif pilih == '2':
        print(f"Mrs. Johnson: 'Ya, ada suara musik keras dari rumah Mr. Smith sekitar pukul 20:00. Musik klasik Beethoven, seperti yang sering dia putar saat malam hujan. Tapi malam itu lebih keras dari biasanya, seolah dia ingin menutupi sesuatu. Saya hampir protes, tapi saya diam saja, Detektif {nama}.'")
        print("Anda merasa ini menarik, mungkin musik digunakan untuk mengalihkan perhatian.")
    else:
        print(f"Mrs. Johnson: 'Mr. Smith orang baik, selalu membantu tetangga, tapi sering bertengkar dengan keluarganya, terutama anaknya John. Mereka ribut soal uang dan warisan. Saya sering mendengar teriakan dari rumah mereka, terutama malam minggu. John selalu minta uang, tapi ayahnya keras. Tolong selesaikan ini, Detektif {nama}.'")
        clues += 1
        print("Informasi ini menambah kecurigaan pada keluarga korban, terutama motif uang.")

    # Saksi 2: Pelayan
    print("\nAnda pergi ke rumah korban dan menemui pelayan rumah, Anna, yang sedang duduk di dapur dengan mata sembab dan secangkir teh dingin di tangan.")
    print(f"Anna: 'Saya bekerja di sini selama 5 tahun, tuan selalu baik. Detektif {nama}, saya sedang membersihkan dapur saat itu, mencuci piring dari makan malam. Tiba-tiba saya mendengar suara dari ruang tamu, seperti orang jatuh atau sesuatu pecah, mungkin gelas. Saya takut dan tidak berani keluar, jantung saya berdegup kencang.'")
    print("Pilihan dialog:")
    print("1. Tanya apa yang Anda lakukan setelah itu.")
    print("2. Tanya apakah Anda melihat siapa pun.")
    print("3. Tanya tentang kebiasaan korban.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Anna: 'Setelah itu, saya pergi ke kamar saya di lantai atas. Pintu rumah terkunci dari dalam, jadi saya pikir aman. Saya tidur dengan gelisah, tapi pagi hari saya menemukan mayat tuan di ruang tamu. Darah di karpet, dan pisau dapur hilang. Saya langsung panggil polisi.'")
        print("Anda merasa ada yang aneh dengan pintu terkunci, mungkin ada cara masuk lain.")
    elif pilih == '2':
        print("Anna: 'Saya melihat anak tuan, John, pulang larut malam itu. Dia masuk melalui pintu belakang sekitar pukul 21:30, basah kuyup karena hujan. Dia terlihat marah, wajahnya merah, dan langsung naik ke kamar tanpa menyapa. Saya dengar dia menggerutu tentang ayahnya.'")
        clues += 1
        print("Ini clue kuat! John mungkin terlibat, dan waktu kedatangannya mencurigakan.")
    else:
        print("Anna: 'Mr. Smith suka minum sendirian di malam hari. Dia sering duduk di ruang tamu dengan segelas wiski, mendengarkan musik klasik. Kadang-kadang dia bicara sendiri tentang masa lalu, tentang istri yang meninggal dan bisnis yang gagal. Dia bilang hidup ini penuh penyesalan.'")
        print("Kebiasaan ini mungkin tidak terkait langsung, tapi menunjukkan kepribadian korban yang depresif.")

    # Saksi 3: Anak Korban
    print("\nDi ruang tamu rumah korban, Anda menemui anaknya, John, yang duduk dengan tangan menutup wajah, pakaiannya masih basah dari hujan.")
    print("John: 'Ayah saya orang baik, selalu bekerja keras, tapi kami sering bertengkar soal uang. Dia keras kepala dan tidak mau membantu saya dengan utang-utang saya. Saya punya masalah keuangan, pinjam sana sini, tapi dia bilang saya harus mandiri.'")
    print("Pilihan dialog:")
    print("1. Tanya di mana Anda saat kejadian.")
    print("2. Tanya tentang warisan.")
    print("3. Tanya apakah Anda melihat sesuatu.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("John: 'Saya di luar kota untuk urusan bisnis, meeting dengan investor. Saya pulang pukul 22:30 dan menemukan ayah saya sudah tewas. Polisi bilang pintu terkunci dari dalam, jadi mungkin bunuh diri. Tapi ayah saya tidak seperti itu, dia kuat.'")
        print("Alibinya kuat dengan detail meeting, tapi Anda tetap curiga karena motif uang.")
    elif pilih == '2':
        print("John: 'Ayah saya akan mewariskan rumah ini dan sebagian besar hartanya kepada saya. Tapi dia bilang saya harus membuktikan diri dulu, mungkin dengan sukses bisnis. Kami bertengkar hebat minggu lalu, saya bilang dia egois, dia bilang saya pemalas. Itu pertengkaran terakhir.'")
        clues += 1
        print("Motif uang muncul kuat. John memiliki alasan kuat untuk membunuh.")
    else:
        print("John: 'Saya melihat bayangan di jendela ruang tamu saat saya pulang. Mungkin itu ayah saya, atau mungkin bukan. Saya tidak yakin, tapi itu membuat saya takut. Apakah ada orang lain di rumah?'")
        print("Bayangan ini misterius, mungkin ada pelaku lain atau John berbohong.")

    # Saksi 4: Teman Lama Korban
    print("\nAnda menemui teman lama korban, Mr. Davis, di kafe dekat vila. Dia pria tua dengan pipa di mulut, terlihat sedih.")
    print("Mr. Davis: 'Saya kenal Smith sejak kuliah, kami sahabat. Dia cerita banyak tentang hidupnya. Pembunuhan ini syok bagi saya. Dia bilang anaknya John bermasalah, sering minta uang. Tapi Smith takut wariskan semuanya, takut John buang-buang.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang masalah keluarga.")
    print("2. Tanya apakah Smith punya musuh.")
    print("3. Tanya tentang kehidupan pribadi Smith.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Mr. Davis: 'John selalu minta uang, tapi Smith bilang dia harus belajar bertanggung jawab. Mereka bertengkar parah bulan lalu, John ancam pergi selamanya. Smith sedih, bilang anaknya seperti dirinya dulu, tapi lebih buruk.'")
        clues += 1
        print("Konflik keluarga ini mendukung motif John.")
    elif pilih == '2':
        print("Mr. Davis: 'Smith punya musuh di bisnis lama, tapi itu lama. Yang terbaru, mungkin bos John yang marah karena Smith tolak investasi. Tapi saya pikir itu tidak serius.'")
        print("Musuh bisnis mungkin ada, tapi fokus pada keluarga.")
    else:
        print("Mr. Davis: 'Smith duda sejak istri meninggal 10 tahun lalu. Dia fokus kerja, tapi sering sedih. Dia bilang hidup ini sepi tanpa keluarga yang harmonis. Mungkin itu sebab dia keras pada John.'")
        print("Kehidupan pribadi Smith menjelaskan keputusannya.")

    # Tebakan Pelaku
    print("\nSetelah mendengarkan semua saksi, Anda merenung sejenak. Berdasarkan penyelidikan Anda, siapa yang Anda duga sebagai pelaku pembunuhan Mr. Smith?")
    print("Pilihan tersangka dengan pertimbangan:")
    print("1. John (anak korban) - Memiliki motif uang dari warisan, alibi tidak sinkron dengan saksi lain yang melihatnya pulang larut, terlihat marah dan basah hujan.")
    print("2. Anna (pelayan rumah) - Mendengar suara kejadian tapi tidak melihat pelaku, memiliki akses ke rumah tapi tidak ada motif jelas atau kebencian.")
    print("3. Mrs. Johnson (tetangga) - Melihat seseorang masuk rumah tapi deskripsinya samar, tidak ada motif pribadi, hanya tetangga yang khawatir.")
    print("4. Mr. Davis (teman lama) - Mengetahui rahasia keluarga tapi tidak ada bukti keterlibatan langsung, motifnya lemah karena persahabatan lama.")
    tebakan = input("Masukkan nomor dugaan Anda (1-4): ")
    
    if tebakan == '1' and clues >= 3:
        print("\nTebakan Anda benar! Berdasarkan clue yang Anda kumpulkan, Anda menyimpulkan bahwa pelaku adalah anak korban, John, yang membunuh ayahnya untuk warisan. Meskipun alibinya kuat, bukti menunjukkan dia masuk rumah lebih awal dan konflik keluarga mendukung.")
        print("Ending Baik: Kasus terselesaikan, John ditangkap setelah penyelidikan lebih lanjut. Kota kembali aman. Deduksi Anda seperti Shinichi Kudo: Dari alibi John yang rapuh, waktu kedatangan yang tidak cocok, dan motif warisan, Anda menyimpulkan bahwa ia adalah pelaku. Penangkapan dilakukan dengan bukti DNA, dan kasus ini menyoroti pentingnya kesehatan mental.")
    else:
        print("\nTebakan Anda salah atau clue tidak cukup. Mari saya jelaskan apa yang sebenarnya terjadi...")
        print("Narasi Akhir: Pada malam itu, John, anak Mr. Smith, kembali ke vila dengan niat jahat. Ia telah lama iri pada kekayaan ayahnya dan ingin mewarisi semuanya tanpa syarat. Meskipun alibinya mengatakan ia di luar kota, bukti menunjukkan ia pulang lebih awal melalui pintu belakang, yang ia buka sendiri. Ia menusuk ayahnya di ruang tamu saat Mr. Smith sedang minum wiski, lalu mengunci pintu dari dalam untuk menutupi jejak. Musik keras yang diputar John untuk menutupi suara, dan bayangan yang dilihatnya sendiri sebagai alibi palsu. Anna mendengar suara, Mrs. Johnson melihat seseorang tinggi (John), dan Mr. Davis tahu tentang konflik keluarga. Jika Anda mengumpulkan clue lebih baik, Anda bisa menangkapnya. Pelaku lolos, dan misteri vila kuno tetap menjadi legenda gelap.")
        print("Ending Buruk: Kasus tidak terselesaikan, pelaku bebas. Kota dilanda ketakutan.")

def case2(nama):
    print("\n=== Misteri Racun di Kantor Teknologi Bandung - 2024 ===")
    print("Pada malam musim dingin tahun 2024, di gedung kantor perusahaan teknologi yang sibuk, Ms. Lee, seorang analis data berbakat berusia 35 tahun, ditemukan tewas di meja kerjanya pukul 23:00. Ia sering menghadapi diskriminasi gender di dunia kerja pria-dominan, di mana ide-ide wanita sering diabaikan. Tubuhnya lunglai, dengan cangkir kopi tergeletak di samping. Otopsi mengungkap racun kuat dalam sistemnya, namun komputer masih menyala dengan email terbuka yang berisi ancaman samar. Kantor ini penuh dengan persaingan internal dan bias budaya, dan Anda, Detektif, harus menyelidiki melalui percakapan dengan rekan kerja yang mungkin memiliki motif tersembunyi. Pilihan Anda akan menentukan apakah kebenaran terungkap atau misteri tetap abadi, sambil mengangkat isu kesetaraan gender.")
    print("Anda harus menemukan pelaku dengan berinteraksi dengan saksi.")
    time.sleep(2)

    clues = 0

    # Saksi 1: Rekan Kerja
    print("\nAnda tiba di kantor yang sunyi dan gelap. Mr. Brown, rekan kerja korban, duduk di ruang meeting dengan wajah lelah.")
    print(f"Mr. Brown: 'Detektif {nama}, Ms. Lee sedang mengerjakan proyek besar yang bisa membuat perusahaan maju. Tapi ada yang iri dengannya, termasuk saya sendiri. Dia terlalu brilian.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang proyek tersebut.")
    print("2. Tanya siapa yang iri.")
    print("3. Tanya apakah Anda melihat seseorang.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print(f"Mr. Brown: 'Proyek itu rahasia, melibatkan AI untuk analisis data. Ms. Lee sering kerja lembur sampai larut malam, bahkan tidur di kantor. Dia bilang ini akan mengubah kariernya, mungkin jadi direktur. Saya dengar bosnya marah karena proyek ini bisa mengancam posisinya. Ini penting, Detektif {nama}.'")
        print("Anda merasa proyek ini mungkin motif bagi seseorang.")
    elif pilih == '2':
        print(f"Mr. Brown: 'Bosnya sendiri yang iri. Mr. White selalu mempromosikan orang lain, padahal Ms. Lee layak mendapatkannya. Saya dengar mereka bertengkar minggu lalu, White bilang Lee terlalu ambisius. Bahkan ada email ancaman dari White. Tolong selidiki itu, Detektif {nama}.'")
        clues += 1
        print("Ini clue menarik! Bos memiliki motif.")
    else:
        print(f"Mr. Brown: 'Saya melihat sekretaris, Lisa, keluar kantor pukul 22:00. Dia terlihat tergesa-gesa, mungkin membawa sesuatu seperti tas kerja. Mungkin dia antar kopi untuk Lee, tapi waktunya aneh. Saya curiga, Detektif {nama}.'")
        print("Lisa mungkin tahu sesuatu.")

    # Saksi 2: Sekretaris
    print("\nDi ruang kerja korban, Anda menemui sekretaris, Lisa, yang sedang menangis sambil memegang foto Ms. Lee.")
    print(f"Lisa: 'Detektif {nama}, saya membawa kopi untuk Ms. Lee seperti biasa. Mungkin racun ada di sana. Saya tidak tahu siapa yang bisa melakukan ini.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang kopi.")
    print("2. Tanya hubungan Anda dengan korban.")
    print("3. Tanya apakah Anda tahu siapa pelaku.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print(f"Lisa: 'Kopi itu dari mesin kantor di lantai bawah. Siapa saja bisa mengaksesnya, tapi saya yang bawa. Ms. Lee minum kopi hitam tanpa gula, seperti biasa. Tapi malam itu kopi terasa aneh, katanya pahit. Mungkin sudah diracuni sebelum saya bawa. Tolong selidiki mesin itu, Detektif {nama}.'")
        print("Mesin kopi umum, sulit dilacak.")
    elif pilih == '2':
        print(f"Lisa: 'Kami teman baik. Dia sering cerita tentang tekanan kerja dan bos yang tidak adil. Saya dukung dia, tapi dia bilang bosnya jahat, selalu sabotase kerja orang lain. Ms. Lee bilang dia akan lapor ke HR jika tidak dipromosikan. Saya khawatir dengannya, Detektif {nama}.'")
        print("Hubungan baik, tapi mungkin ada rahasia.")
    else:
        print(f"Lisa: 'Saya curiga pada rekan kerja, Mr. Brown. Dia selalu iri pada Ms. Lee. Tapi saya tidak punya bukti, hanya perasaan. Mungkin bos juga, karena email ancaman itu. Tolong temukan kebenarannya, Detektif {nama}.'")
        clues += 1
        print("Kecurigaan ini menambah daftar tersangka.")

    # Saksi 3: Bos
    print("\nDi kantor bos, Mr. White duduk di balik meja besar dengan ekspresi tenang, tapi mata tajam.")
    print("Mr. White: 'Ms. Lee brilian, tapi saya promosikan orang lain karena alasan perusahaan. Dia marah, tapi itu bisnis.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang promosi.")
    print("2. Tanya alibi Anda.")
    print("3. Tanya tentang email.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Mr. White: 'Ms. Lee marah karena tidak dipromosikan. Dia kirim email ancaman, bilang akan lapor ke atas. Saya bilang itu tidak akan berhasil.'")
        clues += 1
        print("Motif kuat! Email ancaman ini bukti.")
    elif pilih == '2':
        print("Mr. White: 'Saya di rumah sejak pukul 20:00. Istri saya bisa konfirmasi. Saya tidak pernah ke kantor malam itu.'")
        print("Alibi kuat, tapi Anda tetap curiga.")
    else:
        print("Mr. White: 'Email itu tentang pengunduran diri Ms. Lee. Dia bilang akan keluar jika tidak dipromosikan. Tapi saya tolak.'")
        print("Pengunduran diri ini menarik.")

    # Saksi 4: Rekan Kerja Lain
    print("\nAnda menemui rekan kerja lain, Ms. Green, di kafe kantor. Dia wanita muda dengan ekspresi serius.")
    print("Ms. Green: 'Saya kerja di tim yang sama dengan Ms. Lee. Dia genius, tapi bosnya jahat. Saya dengar banyak gosip tentang persaingan. Brown iri, White ambisius, Lisa terlalu dekat dengan Lee.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang gosip kantor.")
    print("2. Tanya apakah Anda melihat sesuatu.")
    print("3. Tanya tentang proyek.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Ms. Green: 'Gosip bilang White sabotase kerja Lee, Brown curiga Lee akan ambil posisinya, Lisa mungkin cemburu karena Lee lebih sukses. Saya sendiri takut, tapi saya tidak terlibat. Kantor ini penuh intrik.'")
        clues += 1
        print("Gosip ini menunjukkan banyak motif di kantor.")
    elif pilih == '2':
        print("Ms. Green: 'Saya melihat White keluar kantor pukul 21:00, padahal dia bilang di rumah. Mungkin dia kembali. Dan Brown terlihat marah setelah meeting dengan Lee.'")
        print("Penglihatan ini menyangkal alibi White.")
    else:
        print("Ms. Green: 'Proyek itu rahasia, tapi Lee bilang itu akan buat dia kaya. White takut kehilangan kontrol perusahaan. Mungkin itu motifnya.'")
        print("Proyek sebagai pusat konflik.")

    # Tebakan Pelaku
    print("\nSetelah mendengarkan semua saksi, Anda merenung di kantor yang sunyi. Berdasarkan penyelidikan Anda, siapa yang Anda duga sebagai pelaku pembunuhan Ms. Lee?")
    print("Pilihan tersangka dengan pertimbangan:")
    print("1. Mr. White (bos) - Memiliki motif iri karena proyek Lee, email ancaman dari dia, alibi rapuh karena dilihat keluar kantor.")
    print("2. Mr. Brown (rekan kerja) - Iri pada kesuksesan Lee, tapi tidak ada bukti langsung, hanya curiga pribadi.")
    print("3. Lisa (sekretaris) - Membawa kopi korban tapi tidak tahu racun, motif lemah, lebih sebagai saksi.")
    print("4. Ms. Green (rekan kerja lain) - Mengetahui gosip kantor tapi tidak terlibat, motif tidak ada.")
    tebakan = input("Masukkan nomor dugaan Anda (1-4): ")
    
    if tebakan == '1' and clues >= 3:
        print("\nTebakan Anda benar! Anda telah mengungkap skandal kantor dengan kecerdasan luar biasa.")
        print("Penjelasan Lengkap: Dengan clue dari Brown tentang iri White, Lisa tentang email ancaman, dan Ms. Green tentang alibi rapuh, Anda menyimpulkan White meracuni kopi Lee di mesin kantor untuk menghentikan proyeknya. Penangkapan White dilakukan setelah email terbukti dari IP rumahnya, dan ia mengaku diinterogasi. Perusahaan membersihkan citra, karyawan lega, dan Anda dipuji sebagai detektif korporat terbaik. Keadilan ditegakkan di dunia bisnis yang keras.")
        print("Ending Baik: Kasus terselesaikan, Mr. White ditangkap. Perusahaan kembali stabil dan inovatif. Deduksi Anda seperti Shinichi Kudo: Dari email ancaman yang berasal dari IP rumah White, alibi rapuhnya yang tidak cocok dengan saksi, dan motif persaingan proyek, Anda menyimpulkan bahwa ia adalah pelaku. Penangkapan dilakukan dengan bukti digital, dan kasus ini menyoroti pentingnya kesetaraan gender.")
    else:
        print("\nTebakan Anda salah atau clue tidak cukup. Mari saya jelaskan apa yang sebenarnya terjadi...")
        print("Narasi Akhir Lengkap: Mr. White, bos yang ambisius dan takut kehilangan kekuasaan, merencanakan pembunuhan Ms. Lee dengan hati-hati. Ia siapkan racun di mesin kopi kantor saat malam, tahu Lee sering lembur. Ia kirim email ancaman untuk menakuti Lee, lalu pura-pura pulang tapi kembali untuk memastikan. Lisa tidak tahu membawa kopi beracun, Brown iri tapi tidak bertindak, Ms. Green lihat White keluar tapi pikir biasa. Jika Anda fokus pada email dan alibi, Anda bisa menangkapnya. Tanpa itu, White lolos, perusahaan bangkrut karena skandal, karyawan kehilangan pekerjaan, dan dunia teknologi dilanda ketidakpercayaan. Misteri ini menunjukkan bahaya persaingan korporat.")
        print("Ending Buruk: Kasus tidak terselesaikan, pelaku bebas. Perusahaan hancur.")

def case3(nama):
    print("\n=== Misteri Tenggelam di Pesta Mewah Bali - 2025 ===")
    print("Di tengah pesta rumah mewah pada malam tahun baru 2025, Alex, seorang pemuda playboy berusia 28 tahun, ditemukan tewas di kolam renang pukul 01:00 dini hari. Ia terjebak dalam budaya konsumtif yang mendorong utang untuk menjaga gaya hidup mewah, masalah sosial yang umum di masyarakat modern. Tubuhnya terapung dengan bekas pukulan di kepala, menunjukkan bahwa tenggelam bukanlah kecelakaan. Pesta ini dihadiri oleh teman-teman dan kenalan yang penuh rahasia, dan Anda, Detektif, harus menggali kebenaran melalui dialog yang penuh intrik. Setiap pertanyaan Anda bisa membuka pintu ke masa lalu yang gelap atau menutupnya selamanya, sambil mempertimbangkan dampak budaya utang.")
    print("Anda harus menemukan pelaku dengan berinteraksi dengan saksi.")
    time.sleep(2)

    clues = 0

    # Saksi 1: Teman
    print("\nDi taman rumah pesta yang masih ramai dengan suara musik, Anda menemui teman korban, Mia, yang sedang minum di sudut.")
    print("Mia: 'Alex sedang bertengkar dengan seseorang sebelum tenggelam. Saya lihat dari jauh, tapi tidak mendengar apa yang dikatakan. Pesta ini gila.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang pertengkaran.")
    print("2. Tanya siapa yang terlibat.")
    print("3. Tanya apakah Anda melihat sesuatu.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Mia: 'Mereka bertengkar tentang uang. Alex bilang dia tidak bisa bayar utang, dan orang itu marah sekali. Saya pikir itu masalah besar.'")
        print("Pertengkaran uang ini bisa jadi motif.")
    elif pilih == '2':
        print("Mia: 'Dengan pacarnya, Jake. Mereka sering bertengkar akhir-akhir ini. Jake bilang Alex boros dan tidak bertanggung jawab.'")
        clues += 1
        print("Jake sebagai tersangka utama muncul.")
    else:
        print("Mia: 'Saya melihat seseorang mendorong Alex ke arah kolam sekitar pukul 00:30. Orang itu tinggi, tapi wajahnya samar karena lampu redup.'")
        print("Dorongan ini mungkin penyebab tenggelam.")

    # Saksi 2: Pacar
    print("\nDi dekat bar pesta, Anda menemui pacar korban, Jake, yang sedang merokok sendirian dengan wajah muram.")
    print("Jake: 'Kami bertengkar malam ini, tapi saya tidak membunuhnya. Saya pergi setelah itu. Ini gila, siapa yang mau bunuh Alex?'")
    print("Pilihan dialog:")
    print("1. Tanya alibi Anda.")
    print("2. Tanya tentang uang.")
    print("3. Tanya apakah Anda melihat pelaku.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Jake: 'Saya pergi setelah bertengkar pukul 00:15. Saya naik taksi pulang. Sopir bisa konfirmasi. Saya tidak kembali.'")
        print("Alibi kuat, tapi Anda tetap waspada.")
    elif pilih == '2':
        print("Jake: 'Alex berutang uang kepada saya, sekitar 5000 dollar. Dia janji bayar minggu depan, tapi selalu menunda. Itu membuat saya marah.'")
        clues += 1
        print("Utang besar ini motif sempurna.")
    else:
        print("Jake: 'Saya melihat Mia dekat kolam setelah saya pergi. Dia terlihat gelisah, mungkin tahu sesuatu. Tapi saya tidak yakin.'")
        print("Mia sekarang juga dicurigai.")

    # Saksi 3: Tamu Lain
    print("\nDi ruang tamu yang penuh tamu, Anda menemui tamu lain, Sam, yang sedang berdansa tapi berhenti saat Anda datang.")
    print("Sam: 'Pesta ini ramai sekali, banyak orang datang dan pergi. Sulit ingat siapa di mana.'")
    print("Pilihan dialog:")
    print("1. Tanya siapa yang terakhir melihat korban.")
    print("2. Tanya tentang minuman.")
    print("3. Tanya apakah Anda tahu motif.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Sam: 'Mia dan Jake yang terakhir lihat Alex. Mereka bicara di dekat kolam sebelum Alex jatuh. Setelah itu, Mia pergi ke dalam rumah.'")
        print("Mia dan Jake lagi-lagi disebutkan.")
    elif pilih == '2':
        print("Sam: 'Alex minum banyak vodka malam itu. Dia mabuk berat, mungkin itu sebabnya dia jatuh ke kolam. Tapi bekas pukulan di kepala aneh.'")
        print("Mabuk bisa jadi faktor, tapi pukulan mencurigakan.")
    else:
        print("Sam: 'Motifnya pasti uang. Alex punya masalah utang dengan banyak orang, termasuk Jake. Siapa tahu siapa yang putus asa.'")
        clues += 1
        print("Motif uang dikonfirmasi.")

    # Saksi 4: Teman Lama
    print("\nAnda menemui teman lama korban, Ryan, di balkon rumah. Dia pria berusia 30-an dengan gelas champagne.")
    print("Ryan: 'Saya kenal Alex sejak kuliah. Dia playboy, selalu punya masalah. Tapi dia baik hati. Pembunuhan ini syok. Saya dengar dia punya utang besar.'")
    print("Pilihan dialog:")
    print("1. Tanya tentang utang.")
    print("2. Tanya apakah Anda melihat sesuatu.")
    print("3. Tanya tentang hubungan dengan korban.")
    pilih = input("Pilih (1-3): ")
    if pilih == '1':
        print("Ryan: 'Alex berutang ke banyak orang, termasuk Jake dan Mia. Dia pinjam untuk bisnis yang gagal. Mungkin seseorang putus asa dan bunuh dia.'")
        clues += 1
        print("Utang sebagai motif utama dikonfirmasi.")
    elif pilih == '2':
        print("Ryan: 'Saya melihat Jake mendorong Alex ke kolam. Tapi saya pikir itu candaan, sampai Alex tidak muncul. Mungkin Jake marah karena utang.'")
        print("Penglihatan ini menunjukkan Jake sebagai pelaku.")
    else:
        print("Ryan: 'Kami teman baik, tapi Alex sering bohong. Dia bilang hidupnya sempurna, tapi sebenarnya berantakan. Mungkin itu sebab dia tenggelam.'")
        print("Kepribadian Alex menjelaskan kejadian.")

    # Tebakan Pelaku
    print("\nSetelah pesta berakhir dan semua saksi didengar, Anda berdiri di kolam renang yang tenang. Berdasarkan penyelidikan Anda, siapa yang Anda duga sebagai pelaku pembunuhan Alex?")
    print("Pilihan tersangka dengan pertimbangan:")
    print("1. Jake (pacar korban) - Memiliki motif utang yang besar, alibi lemah karena pergi setelah bertengkar, dilihat mendorong korban.")
    print("2. Mia (teman korban) - Melihat pertengkaran tapi tidak terlibat langsung, motif lemah, lebih sebagai saksi.")
    print("3. Sam (tamu lain) - Mengetahui motif uang tapi tidak ada bukti keterlibatan, hanya tamu pesta.")
    print("4. Ryan (teman lama) - Melihat dorongan tapi pikir candaan, motif tidak ada, persahabatan lama.")
    tebakan = input("Masukkan nomor dugaan Anda (1-4): ")
    
    if tebakan == '1' and clues >= 3:
        print("\nTebakan Anda benar! Anda telah menyelesaikan tragedi pesta dengan kebijaksanaan.")
        print("Penjelasan Lengkap: Dengan clue dari Mia tentang pertengkaran, Sam tentang motif uang, dan Ryan tentang dorongan Jake, Anda menyimpulkan Jake membunuh Alex karena utang. Ia dorong Alex ke kolam setelah bertengkar, pukul kepalanya untuk memastikan. Penangkapan Jake dilakukan setelah saksi mata dikonfirmasi, dan ia mengaku di pengadilan. Pesta menjadi pelajaran tentang bahaya utang, keluarga Alex lega, dan Anda dianggap pahlawan sosial. Kota belajar tentang pentingnya komunikasi.")
        print("Ending Baik: Kasus terselesaikan, Jake ditangkap. Pesta menjadi kenangan buruk tapi adil. Deduksi Anda seperti Shinichi Kudo: Dari alibi Jake yang lemah setelah bertengkar, saksi yang melihat dorongan, dan motif utang besar, Anda menyimpulkan bahwa ia adalah pelaku. Penangkapan dilakukan dengan konfirmasi saksi, dan kasus ini menyoroti bahaya budaya konsumtif.")
    else:
        print("\nTebakan Anda salah atau clue tidak cukup. Mari saya jelaskan apa yang sebenarnya terjadi...")
        print("Narasi Akhir Lengkap: Jake, pacar Alex yang frustrasi dengan utang yang menumpuk, menjadi pelaku di balik tragedi pesta. Alex berutang 5000 dollar untuk bisnis gagal, dan Jake putus asa setelah bertengkar. Ia dorong Alex ke kolam renang, pukul kepalanya dengan botol untuk memastikan tenggelam, lalu pura-pura pergi dengan taksi. Mia lihat pertengkaran tapi tidak intervensi, Sam dengar tentang utang tapi tidak curiga, Ryan lihat dorongan tapi pikir candaan pesta. Jika Anda perhatikan alibi Jake dan motif utang, Anda bisa menangkapnya. Tanpa itu, Jake lolos, pesta menjadi skandal nasional, keluarga Alex hancur, dan kota dilanda rumor tentang pesta berbahaya. Misteri ini menunjukkan bagaimana utang bisa menghancurkan hidup.")
        print("Ending Buruk: Kasus tidak terselesaikan, pelaku bebas. Kota dilanda rumor.")

if __name__ == "__main__":
    main()