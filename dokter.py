class Dokter:
    def __init__(self, id_dokter, nama, spesialis):
        self.id = id_dokter
        self.nama = nama
        self.spesialis = spesialis

    def info(self):
        return f"{self.id} | {self.nama} | {self.spesialis}"