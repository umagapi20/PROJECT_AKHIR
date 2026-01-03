from rekammedis import RekamMedis

class Pendaftaran:
    def _init_(self):
        self.data = []

    def tambah(self, pasien, dokter, keluhan):
        self.data.append(RekamMedis(pasien, dokter, keluhan))

    def tampilkan(self):
        for r in self.data:
            print(r.info())