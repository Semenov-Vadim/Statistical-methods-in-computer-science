import math	 # для использования log
from scipy import integrate	 # для вычисления интеграла


def B(x, a, b):
	return (x ** (a - 1)) * ((1 - x) ** (b - 1))


def f(x, q):
	numerator = (x ** (q[0] - 1)) * ((1 - x) ** (q[1] - 1))
	denominator = integrate.quad(B, 0, 1, args=(q[0], q[1]))
	return numerator / denominator[0]


if __name__ == "__main__":
	q_0 = [1.1,	1.7]
	q_1 = [1.2,	2]
	alfa = 0.03
	beta = 0.07
	sample = [0.107,	0.4248,	0.04255,	0.2155,	0.1815,	0.09369,	0.6974,	0.002862,	0.4017]

	gh_0 = math.log(beta / (1 - alfa))
	gh_1 = math.log((1 - beta) / alfa)

	print("gh_0: ", gh_0)
	print("gh_1: ", gh_1)

	gamma = []
	flag_result = False
	for i in range(len(sample)):
		if i == 0:
			gamma.append(math.log(f(sample[i], q_1) / f(sample[i], q_0)))
		else:
			gamma_next = gamma[i - 1] + math.log(f(sample[i], q_1) / f(sample[i], q_0))
			gamma.append(gamma_next)

		if gamma[i] <= gh_0:
			flag_result = True
			print("Принимаем гипотезу Н_0")
			break
		elif gamma[i] >= gh_1:
			flag_result = True
			print("Принимаем гипотезу Н_1")
			break

	print("gamma: ", gamma)
	if not flag_result:
		print("Делаем вывод о неопределенности в выборе гипотез.")

