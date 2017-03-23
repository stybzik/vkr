from math import exp

'''otrezki =  [-0.18872664056834659, -0.17760505309201954, -0.16648346561569249, -0.15536187813936547, -0.14424029066303845, -0.13311870318671143, -0.12199711571038437, -0.11087552823405733, -0.099753940757730308, -0.088632353281403287, -0.077510765805076237, -0.066389178328749215, -0.05526759085242218, -0.044146003376095158, -0.033024415899768123, -0.02190282842344109, -0.010781240947114058, 0.00034034652921297211, 0.011461934005540002, 0.022583521481867035, 0.033705108958194063, 0.044826696434521099, 0.055948283910848121, 0.067069871387175156, 0.078191458863502192, 0.089313046339829227, 0.10043463381615625, 0.1115562212924833, 0.12267780876881032, 0.13379939624513734, 0.14492098372146436, 0.15604257119779141, 0.16716415867411843, 0.17828574615044546, 0.18940733362677248, 0.20052892110309953]
empiricheskie =  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 2, 2, 1, 2, 5, 2, 3, 2, 5, 4, 3, 4, 2, 3, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1]
N = sum(empiricheskie)
print(N)
R = [exp(otrezki[i]) for i in range(len(otrezki))]
P = [empiricheskie[i] / N for i in range(len(empiricheskie))]
print('R = ', R[1::])
print('P = ', P)'''
R =  [0.7500493762604046, 0.7637926446463494, 0.7777877330216258, 0.79203925552206, 0.8065519108289879, 0.8213304837183959, 0.8363798466384457, 0.8517049613159049, 0.867310880392013, 0.8832027490883203, 0.8993858069030513, 0.9158653893385504, 0.9326469296603807, 0.9497359606886524, 0.9671381166221782, 0.9848591348960486, 1.0029048580732474, 1.0212812357709247, 1.0399943266219678, 1.0590503002725122, 1.0784554394160548, 1.0982161418648375, 1.118338922659185, 1.138830416215494, 1.1596973785135773, 1.18094668932409, 1.2025853544767682, 1.2246205081702268, 1.2470594153240837, 1.2699094739741799, 1.293178217711688, 1.3168733181669134, 1.3410025875386062, 1.3655739811696184, 1.390595600169754, 1.4160756940866799, 1.4420226636257754, 1.4684450634198172, 1.4953516048494144, 1.5227511589151241, 1.5506527591621901, 1.5790656046588751, 1.6079990630293635, 1.6374626735422368, 1.6674661502555415, 1.6980193852194805, 1.7291324517377922]
P =  [0.0, 0.010416666666666666, 0.0, 0.0, 0.0, 0.0, 0.03125, 0.0, 0.03125, 0.020833333333333332, 0.0, 0.03125, 0.041666666666666664, 0.0625, 0.052083333333333336, 0.052083333333333336, 0.09375, 0.125, 0.08333333333333333, 0.041666666666666664, 0.0625, 0.020833333333333332, 0.0625, 0.0625, 0.0, 0.041666666666666664, 0.020833333333333332, 0.010416666666666666, 0.010416666666666666, 0.010416666666666666, 0.0, 0.0, 0.010416666666666666, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.010416666666666666, 0.0, 0.0, 0.0, 0.0]
T = 0
TT = 0
for i in range(len(P)):
    T += R[i] * P[i]
    TT += R[i] ** 2 * P[i]
print(T, (TT - T ** 2) ** 0.5)
print(exp(0.0114619340055))
#mean =  0.0114619340055
#sko =  0.066729524858
