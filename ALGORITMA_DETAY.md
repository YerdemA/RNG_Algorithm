# Rastgele Sayı Üreteci (RNG) Algoritma Analizi

Bu modül, kriptografik olmayan ancak yüksek istatistiksel dağılım başarısına sahip **Linear Congruential Generator (LCG)** algoritmasının modifiye edilmiş bir versiyonunu kullanır.

## 1. Algoritma Mantığı
Kullanılan yöntem, bir başlangıç değerini (seed) doğrusal bir denklem üzerinden geçirerek bir sonraki sayıyı üretir. Üretilen sayılar, sistem saatinden alınan "epoch" zamanına dayalı olduğu için her çalıştırıldığında farklıdır (Patern Oluşmaz).

**Formül:** $X_{n+1} = (a \cdot X_n + c) \mod m$

Burada:
- **X**: Rastgele sayı durumu (State)
- **m**: Modulus (2^32)
- **a**: Çarpan (1664525)
- **c**: Artış (1013904223)

## 2. İstatistiksel Kalite (0 ve 1 Eşitliği)
Üretilen her büyük tam sayının `mod 2` değeri alınarak 0 veya 1 elde edilir. LCG algoritmaları, doğru katsayılar seçildiğinde (Numerical Recipes standartları) 0 ve 1 dağılımını uzun vadede %50-%50 oranına yaklaştırır.

## 3. Sözde Kod (Pseudocode)

```text
BAŞLA

    SINIF LCG_Ureteci:
        FONKSİYON __init__(tohum):
            EĞER tohum YOKSA:
                durum = ŞU_ANKİ_ZAMAN()
            DEĞİLSE:
                durum = tohum
            
            # Sabitler
            m = 2^32
            a = 1664525
            c = 1013904223

        FONKSİYON sonraki_sayi():
            durum = (a * durum + c) MOD m
            DÖNDÜR durum

    # Ana Akış
    ureteci = LCG_Ureteci()
    Dizi = []
    
    DÖNGÜ (İstenen Uzunluk Kadar):
        Sayi = ureteci.sonraki_sayi()
        Bit = Sayi MOD 2
        Dizi.EKLE(Bit)
    
    YAZDIR Dizi
    KONTROL ET (0 Sayısı == 1 Sayısı)

BİTİR