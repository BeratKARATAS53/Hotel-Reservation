/*BALANCE TABLE*/
/*call addbalance(:balance_money, :balance_date)*/
/*call addbalance(1000, '2016-01-01');*/

/*----------------------------------------------------------------------------------*/
/*HOTEL TABLE*/
/*call addhotel(:name, :address, :telephone, :hotel_info, :star, :hotel_type)*/
call addhotel('Grand Makel Topkapi', 'Maltepe Mah. Serce Kale sok no:1/1, 34010, Istanbul, Turkiye', '+908514694867', 'Wi-Fi, Havuz, Restoran, Klima, Spa', 8, 'Bes Yildizli');
call addhotel('Divan Adana', 'cinarli Mahallesi, Turhan Cemal Beriker, 01120, Adana, Turkiye', '+908513058779', 'Wi-Fi, Havuz, Restoran, Spa', 6, 'Dort Yildizli');
call addhotel('Dedeman Istanbul', 'Yildiz Posta Caddesi 50 Esentepe, 34340, Istanbul, Turkiye', '+908517298390', 'Havuz, Restoran', 7, 'uc Yildizli');
call addhotel('Shimall Hotel', 'Mucahitler Mahallesi, Mahmut Ersoy Cd. No:6, 27090	, Gaziantep, Turkiye', '+908512124661', 'Havuz, Restoran', 3, 'Iki Yildizli');
call addhotel('Hotel Grand Asya', '17 Eylul Mah. Ataturk Cad. No:86, 10100, Bandirma, Turkiye', '+908515782176', 'Havuz, Restoran', 2, 'Bir Yildizli');
call addhotel('Doubletree By Hilton', 'Siraselviler Caddesi No 45/1, 34437, Istanbul, Turkiye', '+908516550459', 'Wi-Fi, Havuz, Restoran, Klima, Spa', 9, 'Bes Yildizli');
call addhotel('Ramada By Wyndham Diyarbakir', 'Firat Mahallesi, Sanliurfa Yolu uzeri, 21090, Diyarbakir, Turkiye', '+908515056465', 'Wi-Fi, Havuz, Restoran, Spa', 5, 'Dort Yildizli');
call addhotel('Hampton By Hilton Kahramanmaras', 'Trabzon Cad No 2, 46100, Kahramanmaras, Turkiye', '+908513869830', 'Wi-Fi, Havuz, Restoran', 4, 'uc Yildizli');
call addhotel('Pine Bay Holiday Resort', 'Camlimani Mevkii, 09400, Kusadasi, Turkiye', '+908518125102', 'Havuz, Restoran', 4, 'Iki Yildizli');
call addhotel('Ramada Encore Izmir', 'Mithatpasa Caddesi 1460, Balcova, 35330, Izmir, Turkiye', '+908516221776', 'Havuz, Restoran', 1, 'Bir Yildizli');

/*----------------------------------------------------------------------------------*/
/*PERSON TABLE*/
/*call addperson(:firstname, :lastname, :passwrd, :mail, :address, :phone, :age, :salary, :username, :hotel_name, :image, :person_type)*/
/*Customer*/
call addperson('Cemre', 'unal', '3kuUyxfI2h', 'unalcemre231@example.com', 'umit Mahallesi No:43 Kemaliye, Erzincan', '+908511295274', 20, 1000, 'UnalCemre', 'Grand Makel Topkapi', null, 'customer');
call addperson('Ceren', 'Keskin', 'JRMm7FD9pz', 'ceren_keskin924@example.com', 'cigdemli Mahallesi No:863 Gurun, Sivas', '+908511281760', 25, 5000, 'ceren_keskin', 'Divan Adana', null, 'customer');
call addperson('Sezen', 'Dogan', 'CQ9LmiDAqB', 'dogansezen@example.com', 'Karakus Caddesi No:480 Kavaklidere, Mugla', '+908512462713', 23, 2000, 'sezen_dogan', 'Dedeman Istanbul', null, 'customer');
call addperson('Hasan', 'Aydin', 'PfrDWox0eE', 'hasan_aydin66@example.com', 'Kumral Bulvari No:897 Dursunbey, Balikesir', '+908516953719', 25, 1500, 'aydin147', 'Shimall Hotel', null, 'customer');
call addperson('Aynur', 'Can', 'qjFZlRi3Y1', 'canaynur843@example.com', 'Ecdat Sokagi No:136 Ugurludag, corum', '+908515917065', 38, 1700, 'aynur_can', 'Hotel Grand Asya', null, 'customer');
call addperson('sukru', 'Tas', 'teYGXPJmCf', 'tassukru822@example.com', 'Molla Bulvari No:506 Merkezefendi, Denizli', '+908515467333', 37, 1900, 'sukru_tas41', 'Doubletree By Hilton', null, 'customer');
call addperson('Gozde', 'Korkmaz', '76YW20vyFx', 'korkmazgozde991@example.com', 'Nazar Mahallesi No:946 Patnos, Agri', '+908519736217', 30, 5500, 'gozde_korkmaz', 'Ramada By Wyndham Diyarbakir', null, 'customer');
call addperson('Kadir', 'Kaya', '9CHsA3GqIe', 'kadir_kaya144@example.com', 'Keklik cesme Mahallesi No:337 Nazilli, Aydin', '+908515477416', 34, 6000, 'kadir444', 'Hampton By Hilton Kahramanmaras', null, 'customer');
call addperson('Sibel', 'Arslan', 'G5qcQx9320', 'arslansibel742@example.com', 'senlik Mahallesi No:914 semdinli, Hakkari', '+908511169165', 40, 2400, 'sibel954', 'Pine Bay Holiday Resort', null, 'customer');
call addperson('Cemal', 'Kose', 'osFMgUyvRt', 'kosecemal@example.com', 'Gazi Emir Sokagi No:349 Develi, Kayseri', '+908516800932', 31, 3000, 'KoseCemal', 'Ramada Encore Izmir', null, 'customer');

/*Employee*/
call addperson('Kubra', 'ozer', 'OyYdHaK8ew', 'ozerkubra789@example.com', 'Fatih Bulvari No:989 Dalaman, Mugla', '+908513178115', 28, 1200, 'kubraozer', 'Grand Makel Topkapi', null, 'employee');
call addperson('Emre', 'Keskin', 'uj6FSTipNh', 'keskinemre858@example.com', 'Sancak Mahallesi No:659 Yenipazar, Bilecik', '131', 21, 398, 'emre1234', 'Divan Adana', null, 'employee');
call addperson('Ugur', 'celik', 'rQjG1W9XpA', 'celikugur@example.com', 'Tomruk Caddesi No:472 Kibriscik, Bolu', '+908512188855', 22, 2214,"UgurCelik", 'Dedeman Istanbul', null, 'employee');
call addperson('Derya', 'Kilic', 'xlLKChDFoS', 'kilicderya923@example.com', 'Kismetli Sokagi No:905 Ardahan', '+908516407009', 42, 2220,"derya_kilic452" ,'Shimall Hotel', null, 'employee');
call addperson('Osman', 'ozdemir', 'UvkK7sBOzl', 'ozdemirosman725@example.com', 'Lalezar Mahallesi No:877 Ermenek, Karaman', '+908517378952', 37, 3000,"OsmanOzdemir", 'Hotel Grand Asya', null, 'employee');
call addperson('Sevilay', 'Gunes', '1yrlUxNzfc', 'sevIlay_gunes694@example.com', 'Sarraf Sokagi No:626 Eleskirt, Agri', '+908515395499', 29, 5000, "GunesSevIlay", 'Doubletree By Hilton', null, 'employee');
call addperson('Esra', 'Kose', 'ICoRPZvNFb', 'esra_kose47@example.com', 'Bahce Caddesi No:104 Foca, Izmir', '+908514200413', 36, 750,"EsraKose", 'Ramada By Wyndham Diyarbakir', null, 'employee');
call addperson('Osman', 'Can', 'uPyFzsHaEJ', 'canosman@example.com', 'cakaloglu Sokagi No:994 Gediz, Kutahya', '+908519684948', 37, 4000, "osman_can", 'Hampton By Hilton Kahramanmaras', null, 'employee');
call addperson('Muge', 'Korkmaz', 'S8U3waMD5n', 'muge_korkmaz905@example.com', 'Doruk Caddesi No:966 Atabey, Isparta', '+908512258909', 32, 2214,"muge417", 'Pine Bay Holiday Resort', null, 'employee');
call addperson('Muhammet', 'Kaya', '8LdupBAW4e', 'muhammet_kaya730@example.com', 'Soylu Caddesi No:157 Alapli, Zonguldak', '+908516145818', 32, 2589 ,"muhammet_kaya", 'Ramada Encore Izmir', null, 'employee');


/*Manager*/
call addperson('Salih', 'Arslan', 'ptsCeUvnOV', 'arslansalih155@example.com', 'Nagehan Caddesi No:713 cavdir, Burdur', '+908512398944', 31, 300, 'SalihArslan', 'Grand Makel Topkapi', null, 'manager');
call addperson('Furkan ', 'Yilmaz', 'wmXZMKiRdx', 'yilmazfurkan351@example.com', 'Pasakoy Caddesi No:903 Altintas, Kutahya', '+908513897931', 39, 222,"furkan_yilmaz38", 'Divan Adana', null, 'manager');
call addperson('Aynur', 'Can', 'ic8LCSD4mN', 'aynur_can621@example.com', 'Kanaryam Mahallesi No:998 Besikduzu, Trabzon', '+908511198666', 25, 800,"CanAynur", 'Dedeman Istanbul', null, 'manager');
call addperson('Pinar', 'ozcan', 'l4aibhdyfm', 'pinar_ozcan9@example.com', 'Merve Caddesi No:44 Aksehir, Konya', '+908518142867', 25, 900,"PinarOzcan", 'Shimall Hotel', null, 'manager');
call addperson('Ayca', 'Bozkurt', 'bfBDd5sywz', 'bozkurtayca@example.com', 'Akcam Bulvari No:304 Alucra, Giresun', '+908515839854', 43, 345,"BozkurtAyca", 'Hotel Grand Asya', null, 'manager');
call addperson('Ismail', 'cakir', '2m0KoB8CpY', 'ismail_cakir999@example.com', 'Ahiler Caddesi No:941 Yedisu, Bingol', '+908515488313', 21, 223,"ismail_cakir", 'Doubletree By Hilton', null, 'manager');
call addperson('Cemal', 'Yildiz', 'lo2A9PqkG7', 'yildizcemal@example.com', 'Hilal Bulvari No:372 Elbeyli, Kilis', '+908514224374', 43, 50,"yildiz804", 'Ramada By Wyndham Diyarbakir', null, 'manager');
call addperson('Nilgun', 'Korkmaz', 'NzieyfbjZS', 'korkmaznilgun981@example.com', 'Namik Kemal Sokagi No:622 Lice, Diyarbakir', '+908518455036', 29, 600,"nilgun_korkmaz397", 'Hampton By Hilton Kahramanmaras', null, 'manager');
call addperson('Hulya', 'Arslan', 'NfdAylgZIT', 'hulya_arslan797@example.com', 'ulku Mahallesi No:787 caycuma, Zonguldak', '+908515129718', 36, 500, "HulyaArslan", 'Pine Bay Holiday Resort', null, 'manager');
call addperson('Aykut', 'Erdogan', 'zaOEdXbKjx', 'aykut_erdogan244@example.com', 'Semerkant Mahallesi No:23 Mut, Mersin', '+908518392822', 26, 450, "AykutErdogan", 'Ramada Encore Izmir', null, 'manager');

/*----------------------------------------------------------------------------------*/
/*ROOM TABLE*/
/*call addroom(:room_info, :room_price, :room_number, :status, :capacity, :image, :feature, :hotel_name, :room_type)*/
call addroom('Kose Oda, Yatak : 2 cift kisilik yatak, Buyukluk : 50 m², Banyo : 1 banyo', 500, 100, 'available', 4, null, 'Ekstra yatak: 1 ek yatak veya 1 bebek yatagi, Manzara : Dag/Pist', 'Grand Makel Topkapi' , 'Special');
call addroom('Suit Oda, Yatak : 2 cift kisilik yatak, 2 tek kisilik yatak, Buyukluk : 70 m², Banyo : 1 banyo', 400, 200, 'available', 6, null, 'Ekstra yatak: 1 bebek yatagi, Manzara : Dag/Pist', 'Divan Adana', 'special');
call addroom('Standart Oda, Yatak : 2 cift kisilik yatak, Buyukluk : 28-32 m², Banyo : 1 banyo', 175, 300, 'available', 4, null, 'Ekstra yatak: 1 ek yatak veya 1 bebek yatagi, Manzara : Dag/Pist', 'Dedeman Istanbul', 'standart');
call addroom('Connection Oda, Yatak : 4 cift kisilik yatak, Buyukluk : 56-64 m², Banyo : 2 banyo', 250, 400, 'available', 8, null, 'Ekstra yatak: 2 ek yatak veya 2 bebek yatagi, Manzara : Dag/Pist', 'Shimall Hotel', 'standart');
call addroom('Kral Dairesi, Yatak : 1 cift kisilik yatak, 4 tek kisilik yatak, Buyukluk : 170 m², Banyo : 2 banyo, 1 tuvalet', 1000, 500, 'available', 11, null, 'Ekstra yatak: 4 ek yatak veya 4 bebek yatagi, Manzara : Deniz', 'Hotel Grand Asya', 'special');
call addroom('Kose Oda, Yatak : 2 cift kisilik yatak, Buyukluk : 50 m², Banyo : 1 banyo', 500, 101, 'not available', 4, null, 'Ekstra yatak: 1 ek yatak veya 1 bebek yatagi, Manzara : Dag/Pist', 'Hotel Grand Asya', 'Special');
call addroom('Suit Oda, Yatak : 2 cift kisilik yatak, 2 tek kisilik yatak, Buyukluk : 70 m², Banyo : 1 banyo', 400, 201, 'not available', 6, null, 'Ekstra yatak: 1 bebek yatagi, Manzara : Dag/Pist', 'Doubletree By Hilton', 'special');
call addroom('Standart Oda, Yatak : 2 cift kisilik yatak, Buyukluk : 28-32 m², Banyo : 1 banyo', 175, 301, 'not available', 4, null, 'Ekstra yatak: 1 ek yatak veya 1 bebek yatagi, Manzara : Dag/Pist', 'Hampton By Hilton Kahramanmaras', 'standart');
call addroom('Connection Oda, Yatak : 4 cift kisilik yatak, Buyukluk : 56-64 m², Banyo : 2 banyo', 250, 401, 'not available', 8, null, 'Ekstra yatak: 2 ek yatak veya 2 bebek yatagi, Manzara : Dag/Pist', 'Pine Bay Holiday Resort', 'standart');
call addroom('Kral Dairesi, Yatak : 1 cift kisilik yatak, 4 tek kisilik yatak, Buyukluk : 170 m², Banyo : 2 banyo, 1 tuvalet', 1000, 501, 'not available', 11, null, 'Ekstra yatak: 4 ek yatak veya 4 bebek yatagi, Manzara : Deniz', 'Ramada Encore Izmir', 'special');


/*----------------------------------------------------------------------------------*/
/*EXTRA_SERVICE TABLE*/
/*call addextraservice(:service, :service_price, :service_point, :hotel_id)*/
call addextraservice('Temizlik', 50, 5, 1, @service_id);
call addextraservice('Tasima', 100, 6, 1, @service_id);
call addextraservice('Wifi', 10 , 9, 1, @service_id);
call addextraservice('Kuru Temizleme', 60, 2, 1, @service_id);
call addextraservice('Kargo', 25, 3, 3, @service_id);
call addextraservice('Temizlik', 50, 5, 3, @service_id);
call addextraservice('Tasima', 100, 4, 5, @service_id);
call addextraservice('wifi', 10, 7, 4, @service_id);
call addextraservice('Kuru Temizleme', 60, 3, 2, @service_id);
call addextraservice('Kargo', 25, 4, 10, @service_id);

/*----------------------------------------------------------------------------------*/
/*FOOD_SERVICE TABLE*/
/*call addfoodservice(:service, :service_price, :service_point, :food_detail, :hotel_id)*/
call addfoodservice('Kahvalti', 30, 9, ' Beyaz Peynir, Kasar Peyniri, Siyah Zeytin, Su Boregi, Sucuk & Salam & Sosis sis, Recel, Yumurta, cay', 1);
call addfoodservice('Aksam yemegi', 50, 7, 'corba, Etli Yemek, Sebzeli Yemek Salata, Icecek', 1);
call addfoodservice('oglen yemegi', 40, 5, 'Borek, Izgara, Icecek, Kofte', 1);
call addfoodservice('Brunch', 65, 10, 'Hamur isleri, Zeytinyaglilar, Aperitifler, Tatlilar, Pastalar, Kuru meyve', 3);
call addfoodservice('Acik Bufe', 100, 8, 'Peynir ve Zeytin cesitleri, Hamur Isleri, Pizza, Pogaca, Borek cesitleri, Kizartma cesitleri, Ayrica Yoresel ve Organik urunler', 5);
call addfoodservice('Tatli Servisi', 75, 6, 'sekerpare, Tulumba, Revani, Baklava, Sutlu Tatlilar', 3);
call addfoodservice('Hint Mutfagi', 200, 3, 'Samosa, Paratha, Biryani, Tandoori', 4);
call addfoodservice('Geleneksel Turk Mutfagi', 350, 10, 'Etli cig kofte, Tas kebabi, Patlican musakka, Mucver, Kebap, Doner', 4);
call addfoodservice('Italyan Mutfagi', 300, 5, 'Pizza, Spagetti, Lazanya, Chicken Parmigiana', 2);
call addfoodservice('Uzak Dogu Mutfagi', 250, 8, 'Sushi,Tom Yum Goong, Dak Kkochi, Kim Chi', 10);

/*----------------------------------------------------------------------------------*/
/*ADD ROOM EXTRA_SERVICE TABLE*/
/*call addroom_extraservice(:room_id, :service_id)*/
call addroom_extraservice(1, 1);
call addroom_extraservice(2, 9);
call addroom_extraservice(3, 8);
call addroom_extraservice(4, 7);
call addroom_extraservice(5, 6);
call addroom_extraservice(6, 5);
call addroom_extraservice(7, 4);
call addroom_extraservice(1, 3);
call addroom_extraservice(1, 2);
call addroom_extraservice(1, 1);

/*----------------------------------------------------------------------------------*/
/*REZERVATION TABLE*/
/*call addreservation(:start_date, :finish_date, :customer_id, :room_number)*/
call addreservation(curdate(), curdate()+1, 1, '1-1-100', 500);
call addreservation(curdate(), curdate()+1, 1, '2-1-200', 500);
call addreservation(curdate()+1, curdate()+2, 2, '1-1-100', 1500);
call addreservation(curdate()-5, curdate()-2, 2, '1-1-100', 500);
call addreservation(curdate()-1, curdate(), 4, '1-1-100', 250);
call addreservation(curdate()-51, curdate()-42, 3, '1-1-100', 175);

/*----------------------------------------------------------------------------------*/
/*ORGANIZATION TABLE*/
/*call addorganization(:name, :org_info, :price, :hotel_name)*/
call addorganization('Toplanti', 'Projeksiyon, Kablolu / Kablosuz Internet Baglantisi, Ses Sistemi, Yazi Tahtasi', 500, null, 'Grand Makel Topkapi');
call addorganization('Dugun', 'Catering, cicek, Davetiye, Dekor, DJ, Fotograf, Nikah sekeri, Pasta', 8000, null, 'Divan Adana');
call addorganization('Mezuniyet', 'Kokteyl, Susleme hizmetleri, Gosteri, Sahne kurulumu, Ses sistemi kurulumu ve DJ hizmeti', 11000, null, 'Dedeman Istanbul');
call addorganization('Balo', 'Guler yuz ve kaliteli hizmet,  yiyecek-icecek temin etme, Susleme hizmetleri', 5000, null, 'Shimall Hotel');
call addorganization('Mevlid', 'Susleme, Hediyelik, Pasta, Kiyafet', 200, null, 'Hotel Grand Asya');

/*----------------------------------------------------------------------------------*/
/*RENT ORGANIZATION TABLE*/
/*call addrentorganization(:customer_id, :organization_id)*/
call addrentorganization(1, 10);
call addrentorganization(2, 9);
call addrentorganization(3, 8);
call addrentorganization(4, 7);
call addrentorganization(5, 6);
call addrentorganization(6, 5);
call addrentorganization(7, 4);
call addrentorganization(8, 3);
call addrentorganization(9, 2);
call addrentorganization(10, 1);

