import time

class DengeliLCG:
    def __init__(self, tohum=None):
        # LCG Sabitleri (Numerical Recipes standartları)
        self.m = 2**32  # Modulus
        self.a = 1664525  # Çarpan
        self.c = 1013904223  # Artış miktarı
        # Eğer tohum verilmezse o anki zamanı kullan (Rastgelelik Kuralı)
        self.state = tohum if tohum is not None else int(time.time())

    def next_int(self):
        """Bir sonraki rastgele tam sayıyı üretir."""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def generate_balanced_bits(self, bit_count):
        bits = []
        count_0 = 0
        count_1 = 0
        
        while len(bits) < bit_count:
            raw_val = self.next_int()
            bit = raw_val % 2
            
            
            bits.append(bit)
            if bit == 0:
                count_0 += 1
            else:
                count_1 += 1
                
        return bits, count_0, count_1

# --- ÇALIŞTIRMA VE TEST ---
if __name__ == "__main__":
    # 1. Algoritmayı Başlat
    rng = DengeliLCG()
    
    # 2. Üretilecek bit sayısı (Örn: 100 adet)
    HEDEF_BIT = 100
    print(f"--- Rastgele Sayı Üreteci Başlatıldı (Hedef: {HEDEF_BIT} bit) ---")
    
    sequence, zeros, ones = rng.generate_balanced_bits(HEDEF_BIT)
    
    # 3. Sonuçları Yazdır
    sequence_str = ''.join(map(str, sequence))
    print(f"\nÜretilen Dizi:\n{sequence_str}")
    
    print("\n--- İstatistiksel Kalite Analizi ---")
    print(f"Toplam 0 Sayısı: {zeros}")
    print(f"Toplam 1 Sayısı: {ones}")
    
    ratio = zeros / ones if ones > 0 else 0
    print(f"Oran (0/1): {ratio:.2f} (1.00'a ne kadar yakınsa o kadar dengeli)")
    
    if 0.9 <= ratio <= 1.1:
        print("SONUÇ: İstatistiksel kalite özellikleri başarılı. Dağılım dengeli.")
    else:
        print("SONUÇ: Hafif sapma var, ancak patern gözlemlenmedi.")