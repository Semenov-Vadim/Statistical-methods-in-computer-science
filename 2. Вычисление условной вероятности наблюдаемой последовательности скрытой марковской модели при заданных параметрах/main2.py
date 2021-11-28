

if __name__ == "__main__":
	list_o = [1,	4,	4,	1,	4,	5,	3,	1,	3,	1,	3,	2,	5,	5,	5,	2,	2,	3]
	list_a = [[0.105309675,	0.297780002,	0.213051211,	0.077142111,	0.306717001],
			[0.187760676,	0.215099934,	0.168318753,	0.311627628,	0.117193009],
			[0.074311243,	0.194925111,	0.04648007,		0.462151852,	0.222131724],
			[0.128525766,	0.179217357,	0.25736239,		0.285348733,	0.149545754],
			[0.235152482,	0.389382181,	0.062794844,	0.283916338,	0.028754154]]
	list_b = [[0.1553,	0.1609,	0.1112,	0.2896,	0.2830],
			[0.2365,	0.2780,	0.1329,	0.2140,	0.1386],
			[0.3664,	0.1948,	0.1499,	0.1789,	0.1100],
			[0.1454,	0.3011,	0.0072,	0.2698,	0.2766],
			[0.4244,	0.1087,	0.2441,	0.1982,	0.0245]]
	list_pi = [0.2272,	0.1109,	0.3213,	0.2675,	0.0731]

	alpha = []
	for i in range(len(list_o)):
		alpha.append([])


	t = 0

	for a in range(len(alpha)):
		if a == 0:
			""" Initialization:"""
			for i in range(len(list_pi)):
				temp = list_pi[i] * list_b[i][list_o[0] - 1]
				alpha[0].append(temp)
		else:
			"""Induction:"""
			t += 1
			for j in range(len(list_pi)):
				sum_alpha_a = 0
				for i in range(len(list_pi)):
					sum_alpha_a += (alpha[t-1][i] * list_a[i][j])
				alpha[a].append(sum_alpha_a * list_b[j][list_o[t] - 1])

	pr_o_lambda = 0
	for i in alpha[len(alpha) - 1]:
		pr_o_lambda += i

	print("matrix α:")
	for i in alpha:
		print(i)

	print("\n\n")
	print("Pr(O|λ)=", pr_o_lambda)

