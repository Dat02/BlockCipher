# BlockCipher

Cài đặt sơ đồ mã hóa và giải mã cho:
  - CBC_AES mode
  - CTR_AES mode
  - 

Cả 2 đều dùng block cipher với key = 16 bytes, padding: pkcs#7, hàm sinh số ngẫu nhiên urandom.

Bài toán được cài đặt bởi Crypto package của python, hàm sinh số ngẫu nhiên os.urandom. Có thể thay đổi data (plaintext) và key trong hàm main để thử
