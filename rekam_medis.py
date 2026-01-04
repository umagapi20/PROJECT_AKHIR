class RekamMedis:
    def _init_(self, pasien, dokter, keluhan):
        self.pasien = pasien
        self.dokter = dokter
        self.keluhan = keluhan

    def info(self):
        return f"{self.pasien.nama} | {self.dokter.nama} | {self.keluhan}"