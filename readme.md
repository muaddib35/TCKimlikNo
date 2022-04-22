# T.C. Kimlik No Doğrulama Fonksiyonu

## Açıklama
    TC Kimlik nonun doğrulanması için uyması gereken şartlar şunlardır:

    1. 11 hane olmalıdır.
    2. Her hanesi rakam olmalıdır.
    2. İlk hane 0 olamaz.
    3. 1, 3, 5, 7, 9 uncu sayıların toplamının yedi katından 2,4,6,8 inci sayıların toplamının farkı çıkarıldığında mod10'u 10'uncu rakamı verir.
    4. İlk 10 rakamın toplamının mod 10'u 11. rakamı vermelidir.


## Örnek
Örnek kullanım şu şekildedir. 

```
    import verify_turkish_citizen_id from turkishcitizennumber

    tckimlik_no = 12345678901
    if verify_turkish_citizen_id(tckimlik_no):
        return 'TC Kimlik No Doğrulandı'
    else:
        return 'TC Kimlik No Hatalı'
 
 ```

