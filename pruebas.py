import math
import unittest
import libreria


class TestLibreria(unittest.TestCase):

    def test_sumaVec(self):
        self.assertEqual(libreria.suma([1+2j,4+5j,7+8j],[1+2j,4+5j,7+8j]),[2+4j,8+10j,14+16j],msg="Equal")
        self.assertEqual(libreria.suma([2+4j,2+4j,2+4j],[2+4j,2+4j,2+4j]),[4+8j,4+8j,4+8j], msg="Equal")

    def test_inversoVec(self):
        self.assertEqual(libreria.inverso([1+2j,4+5j,7+8j]),[(-1-2j),(-4-5j),(-7-8j)],msg="Equal")

    def test_multEscalar(self):
        self.assertEqual(libreria.multEscalar(2,[1+2j,4+5j,7+8j]),[2+4j,8+10j,14+16j],msg="Equal")

    def test_sumaMat(self):
        self.assertEqual(libreria.sumaMat([[1+2j,4+5j],[6+7j,8+9j]],[[1+2j,4+5j],[6+7j,8+9j]]),[[2+4j,8+10j],[12+14j,16+18j]],msg="Equal")

    def test_inversaMat(self):
        self.assertEqual(libreria.inversaMat([[1+2j,4+5j],[6+7j,8+9j]]),[[-1-2j,-4-5j],[-6-7j,-8-9j]],msg="Equal")

    def test_multMat(self):
        self.assertEqual(libreria.multMat(2,[[1+2j,4+5j],[6+7j,8+9j]]),[[2+4j,8+10j],[12+14j,16+18j]],msg="Equal")

    def test_transpuestaMat(self):
        self.assertEqual(libreria.transpuestaMat([[1+2j,4+5j],[6+7j,8+9j]]),[[1+2j,6+7j],[4+5j,8+9j]],msg="Equal")

    def test_conjugadaMat(self):
        self.assertEqual(libreria.conjugadaMat([[1+2j,4+5j],[6+7j,8+9j]]),[[1-2j,4-5j],[6-7j,8-9j]],msg="Equal")

    def test_adjuntaMat(self):
        self.assertEqual(libreria.adjuntaMat([[1+2j,4+5j],[6+7j,8+9j]]),[[1-2j,6-7j],[4-5j,8-9j]],msg="Equal")

    def test_productoMat(self):
        self.assertEqual(libreria.productoMat([[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1],[1,1,1]]),[[3,3,3],[3,3,3],[3,3,3]],msg="Equal")

    def test_internoVec(self):
        self.assertEqual(libreria.internoVec([1,2,3],[4,5,6]),32,msg="Equal")

    def test_normaVec(self):
        self.assertEqual(libreria.normaVec([1,1,1,1]),2,msg="Equal")

    def test_distanciaVec(self):
        self.assertEqual(libreria.distanciaVec([1,2,3],[4,5,6]),math.sqrt(27),msg="Equal")

    def test_unitaria(self):
        self.assertEqual(libreria.unitaria([[1,0,0],[0,1,0],[0,0,1]]),True,msg="Equal")
        self.assertEqual(libreria.unitaria([[1,0,5],[0,1,0],[1,0,1]]), False, msg="Equal")

    def test_hermitiana(self):
        self.assertEqual(libreria.hermitiana([[5,3+5j],[3-5j,1]]),True,msg="Equal")
        self.assertEqual(libreria.hermitiana([[1,0,5],[0,1,0],[1,0,1]]), False, msg="Equal")

    def test_productoTensor(self):
        self.assertEqual(libreria.productoTensor([[1,1],[1,1]],[[1,1],[1,1]]),None, msg="Equal")

if __name__ == "__main__":
    unittest.main()