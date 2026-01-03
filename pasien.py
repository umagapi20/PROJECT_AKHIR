class Pasien:
    def _init_(self, id_pasien, nama, umur):
        self.id = id_pasien
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"{self.id} | {self.nama} | {self.umur} tahun"