class Config(object):
	def __init__(self):
		# 
		self.AREA_SIZE      = [224, 224]
		self.AREA_SIZE_2    = [int(item /  2) for item in self.AREA_SIZE]
		self.AREA_SIZE_4    = [int(item /  4) for item in self.AREA_SIZE]
		self.AREA_SIZE_8    = [int(item /  8) for item in self.AREA_SIZE]
		self.AREA_SIZE_16   = [int(item / 16) for item in self.AREA_SIZE]
		self.AREA_SIZE_32   = [int(item / 32) for item in self.AREA_SIZE]

		self.TABLEAU20 = [
			(174, 199, 232), (255, 187, 120), (152, 223, 138), (255, 152, 150), (197, 176, 213),
			(196, 156, 148), (247, 182, 210), (199, 199, 199), (219, 219, 141), (158, 218, 229),
		]
		# Blu Org Grn Red Prp
		# Brn Pnk Gry Ylw Aoi
		self.TABLEAU20_DEEP = [
			( 31, 119, 180), (255, 127,  14), ( 44, 160,  44), (214,  39,  40), (148, 103, 189),
			(140,  86,  75), (227, 119, 194), (127, 127, 127), (188, 189,  34), ( 23, 190, 207),
		]

		# Learning parameters
		self.NUM_ITER = 2000001
		self.LEARNING_RATE = 5e-6
		self.V_OUT_RES = tuple(self.AREA_SIZE_8)
		self.AREA_TRAIN_BATCH = 4
		self.AREA_VALID_BATCH = 6
		self.AREA_TEST_BATCH = 12
		self.SIM_TRAIN_BATCH = 64
		self.SIM_TRAIN_POS_TH = 0.7
