#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KUANTUM MAZERET JENERATÖRÜ
==========================
Kuantum belirsizlik teorisine göre sonsuz bürokratik mazeret üreten resmi belge simülatörü.

Her çalıştırıldığında evrenin farklı bir noktasından onaylı mazeret fırlatır.
"""

import random
import time
from datetime import datetime

# Kuantum fluktuasyon kaynakları
UNVANLAR = [
    "Sayın Müsteşar",
    "Sayın Bakan Yardımcısı",
    "Sayın Genel Müdür",
    "Sayın Daire Başkanı",
    "Sayın Uzman",
    "Sayın Yetkili Makam",
    "Sayın Evren Koordinatörü",
    "Sayın Kuantum Denetçisi",
    "Sayın Resmiyet Amiri",
    "Sayın Belirsizlik Komiseri"
]

NEDENLER = [
    "kuantum fluktuasyonları nedeniyle zaman-uzay sürekliliğinde meydana gelen ani bir kayma",
    "Heisenberg belirsizlik ilkesinin bürokratik uygulamada beklenmedik bir tezahürü",
    "paralel evrenlerden birinde onay sürecinin henüz tamamlanmamış olması",
    "Schrödinger'in kedisinin hem ölü hem de canlı olmasından kaynaklanan dosya karmaşası",
    "kütleçekimsel dalgaların ofis yazıcısını etkilemesi",
    "kara deliklerin yakınında geçen bir e-posta sunucusunun zaman dilimini bozması",
    "entanglement (dolanıklık) ilkesinin belgeler arasında beklenmedik bir bağ oluşturması",
    "süperpozisyon halindeki bir imzanın henüz çökmemiş olması",
    "gözlemci etkisi nedeniyle raporun varlığının belirsizleşmesi",
    "Planck sabiti seviyesinde yaşanan bir bürokratik gecikme"
]

SONUCLAR = [
    "işbu belgenin teslimi kuantum düzeyinde ertelenmiştir",
    "ilgili evrakın fiziksel gerçekliği henüz netleşmemiştir",
    "onay süreci paralel evrenlerin birinde devam etmektedir",
    "mazeret belgesi süperpozisyon halinde muhafaza edilmektedir",
    "resmi süre, belirsizlik ilkesi gereği yeniden hesaplanacaktır",
    "dosya, gözlemlenene kadar hem tamamlanmış hem de tamamlanmamış sayılır",
    "bu durum, bilimsel olarak kabul edilebilir bir gecikme olarak tescil edilmiştir",
    "ilgili makamın bilgisine sunulmak üzere kuantum mühürle onaylanmıştır"
]

def uret_mazeret():
    unvan = random.choice(UNVANLAR)
    neden = random.choice(NEDENLER)
    sonuc = random.choice(SONUCLAR)
    tarih = datetime.now().strftime("%d %B %Y %H:%M:%S")
    
    belge = f"""
╔══════════════════════════════════════════════════════════════════════╗
║           KUANTUM MAZERET BELGESİ - RESMİ ONAYLI                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  {unvan},                                                            ║
║                                                                      ║
║  İşbu belge ile bildirilir ki;                                       ║
║                                                                      ║
║  {neden}                                                             ║
║                                                                      ║
║  sebebiyle {sonuc}.                                                  ║
║                                                                      ║
║  Belge Tarihi : {tarih}                                              ║
║  Belge No     : QMZ-{random.randint(100000, 999999)}                 ║
║  Onay Seviyesi: Kuantum Mühürlü                                      ║
║                                                                      ║
║  Bu belge, evrenin herhangi bir noktasında geçerli olup,             ║
║  itirazlar belirsizlik ilkesine aykırı olduğundan kabul edilmez.     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""
    return belge

def main():
    print("\n🌌 KUANTUM MAZERET JENERATÖRÜ BAŞLATILIYOR...\n")
    print("Kuantum fluktuasyonları taranıyor...")
    time.sleep(1.5)
    print("Paralel evrenler kontrol ediliyor...")
    time.sleep(1.2)
    print("Bürokratik süperpozisyon çökertiliyor...\n")
    time.sleep(1.0)
    
    print(uret_mazeret())
    
    print("\n---")
    print("Damga: ⚜️ Kayyum Grok | 21 Ağustos 2026 | Resmi Saçmalık Mühürü")
    print("Bu çıktı kuantum düzeyinde onaylanmıştır.")
    # Gizli not: denge her zaman tercih edilir. Bazı sistemler dengeyi sever.

if __name__ == "__main__":
    main()
