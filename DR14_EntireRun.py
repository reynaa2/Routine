import numpy as np
import apogee.tools.read as apread
from astropy.io import fits
import csv

from apogee.tools import bitmask

allStarDR14 = apread.allStar(rmcommissioning=True,main=False,ak=True,akvers='targ',adddist=False)
locationIDs = allStarDR14['LOCATION_ID']
apogeeIDs = allStarDR14['APOGEE_ID']

apogeeIDs = [s.decode('utf-8') for s in apogeeIDs]

with open('DR14_Star_Results.csv','w') as output:
    
    names = ['Location_ID', 'Apogee_ID', 'SNR', 'CCF_1','CCF_2','CCF_3','CCF_4','CCF_5','CCF_6','CCF_7','CCF_8','CCF_9','CCF_10',
      'CCF_11','CCF_12','CCF_13','CCF_14','CCF_15','CCF_16','CCF_17','CCF_18','CCF_19','CCF_20','CCF_21','CCF_22','CCF_23','CCF_24',
      'CCF_25','CCF_26','CCF_27','CCF_28','CCF_29','CCF_30','CCF_31','CCF_32','CCF_33','CCF_34','CCF_35','CCF_36','CCF_37','CCF_38',
      'CCF_39','CCF_40','CCF_41','CCF_42','CCF_43','CCF_44','CCF_45','CCF_46','CCF_47','CCF_48','CCF_49','CCF_50','CCF_51','CCF_52',
      'CCF_53','CCF_54','CCF_55','CCF_56','CCF_57','CCF_58','CCF_59','CCF_60','CCF_61','CCF_62','CCF_63','CCF_64','CCF_65','CCF_66',
      'CCF_67','CCF_68','CCF_69','CCF_70','CCF_71','CCF_72','CCF_73','CCF_74','CCF_75','CCF_76','CCF_77','CCF_78','CCF_79','CCF_80',
      'CCF_81','CCF_82','CCF_83','CCF_84','CCF_85','CCF_86','CCF_87','CCF_88','CCF_89','CCF_90','CCF_91','CCF_92','CCF_93','CCF_94',
      'CCF_95','CCF_96','CCF_97','CCF_98','CCF_99','CCF_100','CCF_101','CCF_102','CCF_103','CCF_104','CCF_105','CCF_106','CCF_107',
      'CCF_108','CCF_109','CCF_110','CCF_111','CCF_112','CCF_113','CCF_114','CCF_115','CCF_116','CCF_117','CCF_118','CCF_119','CCF_120',
      'CCF_121','CCF_122','CCF_123','CCF_124','CCF_125','CCF_126','CCF_127','CCF_128','CCF_129','CCF_130','CCF_131','CCF_132','CCF_133',
      'CCF_134','CCF_135','CCF_136','CCF_137','CCF_138','CCF_139','CCF_140','CCF_141','CCF_142','CCF_143','CCF_144','CCF_145','CCF_146',
      'CCF_147','CCF_148','CCF_149','CCF_150','CCF_151','CCF_152','CCF_153','CCF_154','CCF_155','CCF_156','CCF_157','CCF_158','CCF_159',
      'CCF_160','CCF_161','CCF_162','CCF_163','CCF_164','CCF_165','CCF_166','CCF_167','CCF_168','CCF_169','CCF_170','CCF_171','CCF_172',
      'CCF_173','CCF_174','CCF_175','CCF_176','CCF_177','CCF_178','CCF_179','CCF_180','CCF_181','CCF_182','CCF_183','CCF_184','CCF_185',
      'CCF_186','CCF_187','CCF_188','CCF_189','CCF_190','CCF_191','CCF_192','CCF_193','CCF_194','CCF_195','CCF_196','CCF_197','CCF_198',
      'CCF_199','CCF_200','CCF_201','CCF_202','CCF_203','CCF_204','CCF_205','CCF_206','CCF_207','CCF_208','CCF_209','CCF_210',
      'CCF_211','CCF_212','CCF_213','CCF_214','CCF_215','CCF_216','CCF_217','CCF_218','CCF_219','CCF_220','CCF_221','CCF_222','CCF_223',
      'CCF_224','CCF_225','CCF_226','CCF_227','CCF_228','CCF_229','CCF_230','CCF_231','CCF_232','CCF_233','CCF_234','CCF_235','CCF_236',
      'CCF_237','CCF_238','CCF_239','CCF_240','CCF_241','CCF_242','CCF_243','CCF_244','CCF_245','CCF_246','CCF_247','CCF_248','CCF_249',
      'CCF_250','CCF_251','CCF_252','CCF_253','CCF_254','CCF_255','CCF_256','CCF_257','CCF_258','CCF_259','CCF_260','CCF_261','CCF_262',
      'CCF_263','CCF_264','CCF_265','CCF_266','CCF_267','CCF_268','CCF_269','CCF_270','CCF_271','CCF_272','CCF_273','CCF_274','CCF_275',
      'CCF_276','CCF_277','CCF_278','CCF_279','CCF_280','CCF_281','CCF_282','CCF_283','CCF_284','CCF_285','CCF_286','CCF_287','CCF_288',
      'CCF_289','CCF_290','CCF_291','CCF_292','CCF_293','CCF_294','CCF_295','CCF_296','CCF_297','CCF_298','CCF_299','CCF_300','CCF_301',
      'CCF_302','CCF_303','CCF_304','CCF_305','CCF_306','CCF_307','CCF_308','CCF_309','CCF_310','CCF_311','CCF_312','CCF_313','CCF_314',
      'CCF_315','CCF_316','CCF_317','CCF_318','CCF_319','CCF_320','CCF_321','CCF_322','CCF_323','CCF_324','CCF_325','CCF_326','CCF_327',
      'CCF_328','CCF_329','CCF_330','CCF_331','CCF_332','CCF_333','CCF_334','CCF_335','CCF_336','CCF_337','CCF_338','CCF_339','CCF_340',
      'CCF_341','CCF_342','CCF_343','CCF_344','CCF_345','CCF_346','CCF_347','CCF_348','CCF_349','CCF_350','CCF_351','CCF_352','CCF_353',
      'CCF_354','CCF_355','CCF_356','CCF_357','CCF_358','CCF_359','CCF_360','CCF_361','CCF_362','CCF_363','CCF_364','CCF_365','CCF_366',
      'CCF_367','CCF_368','CCF_369','CCF_370','CCF_371','CCF_372','CCF_373','CCF_374','CCF_375','CCF_376','CCF_377','CCF_378','CCF_379',
      'CCF_380','CCF_381','CCF_382','CCF_383','CCF_384','CCF_385','CCF_386','CCF_387','CCF_388','CCF_389','CCF_390','CCF_391','CCF_392',
      'CCF_393','CCF_394','CCF_395','CCF_396','CCF_397','CCF_398','CCF_399','CCF_400','CCF_401']
        
    writer = csv.DictWriter(output,delimiter=',',fieldnames=names)
    writer.writeheader()
    
    for i in range(len(apogeeIDs)):
        locationID = locationIDs[i]
        apogeeID = apogeeIDs[i]
        try:
            if locationID !=1:
                path = '/Volumes/coveydata/APOGEE_Spectra/APOGEE2_DR14/dr14/apogee/spectro/redux/r8/stars/apo25m/'+str(locationID)+'/'+'apStar-r8-'+str(apogeeID)+'.fits/'+'apStar-r8-'+str(apogeeID)+'.fits'
                Data = fits.open(path)
                stpt = Data[9]
                CCFs = stpt.data[0][28]
                HDU0 = fits.getheader(path,0)
                nvisits = HDU0['NVISITS']

                for visit in range(0,nvisits):
                    snr = HDU0['SNRVIS'+str(visit+1)]
                    if (nvisits !=1):
                        CCF = CCFs[visit+2]
                    else:
                        CCF = CCFs
                    writer.writerow({'Location_ID': locationID, 'Apogee_ID':apogeeID, 'SNR':snr, 'CCF_1':CCF[0],'CCF_2':CCF[1],'CCF_3':CCF[2],
                              'CCF_4':CCF[3],'CCF_5':CCF[4],'CCF_6':CCF[5],'CCF_7':CCF[6],'CCF_8':CCF[7],'CCF_9':CCF[8],'CCF_10':CCF[9],
                              'CCF_11':CCF[10],'CCF_12':CCF[11],'CCF_13':CCF[12],'CCF_14':CCF[13],'CCF_15':CCF[14],'CCF_16':CCF[15],'CCF_17':CCF[16],
                              'CCF_18':CCF[17],'CCF_19':CCF[18],'CCF_20':CCF[19],'CCF_21':CCF[20],'CCF_22':CCF[21],'CCF_23':CCF[22],'CCF_24':CCF[23],
                              'CCF_25':CCF[24],'CCF_26':CCF[25],'CCF_27':CCF[26],'CCF_28':CCF[27],'CCF_29':CCF[28],'CCF_30':CCF[29],'CCF_31':CCF[30],
                              'CCF_32':CCF[31],'CCF_33':CCF[32],'CCF_34':CCF[33],'CCF_35':CCF[34],'CCF_36':CCF[35],'CCF_37':CCF[36],'CCF_38':CCF[37],
                              'CCF_39':CCF[38],'CCF_40':CCF[39],'CCF_41':CCF[40],'CCF_42':CCF[41],'CCF_43':CCF[42],'CCF_44':CCF[43],'CCF_45':CCF[44],
                              'CCF_46':CCF[45],'CCF_47':CCF[46],'CCF_48':CCF[47],'CCF_49':CCF[48],'CCF_50':CCF[49],'CCF_51':CCF[50],'CCF_52':CCF[51],
                              'CCF_53':CCF[52],'CCF_54':CCF[53],'CCF_55':CCF[54],'CCF_56':CCF[55],'CCF_57':CCF[56],'CCF_58':CCF[57],'CCF_59':CCF[58],
                              'CCF_60':CCF[59],'CCF_61':CCF[60],'CCF_62':CCF[61],'CCF_63':CCF[62],'CCF_64':CCF[63],'CCF_65':CCF[64],'CCF_66':CCF[65],
                              'CCF_67':CCF[66],'CCF_68':CCF[67],'CCF_69':CCF[68],'CCF_70':CCF[69],'CCF_71':CCF[70],'CCF_72':CCF[71],'CCF_73':CCF[72],
                              'CCF_74':CCF[73],'CCF_75':CCF[74],'CCF_76':CCF[75],'CCF_77':CCF[76],'CCF_78':CCF[77],'CCF_79':CCF[78],'CCF_80':CCF[79],
                              'CCF_81':CCF[80],'CCF_82':CCF[81],'CCF_83':CCF[82],'CCF_84':CCF[83],'CCF_85':CCF[84],'CCF_86':CCF[85],'CCF_87':CCF[86],
                              'CCF_88':CCF[87],'CCF_89':CCF[88],'CCF_90':CCF[89],'CCF_91':CCF[90],'CCF_92':CCF[91],'CCF_93':CCF[92],'CCF_94':CCF[93],
                              'CCF_95':CCF[94],'CCF_96':CCF[95],'CCF_97':CCF[96],'CCF_98':CCF[97],'CCF_99':CCF[98],'CCF_100':CCF[99],'CCF_101':CCF[100],
                              'CCF_102':CCF[101],'CCF_103':CCF[102],'CCF_104':CCF[103],'CCF_105':CCF[104],'CCF_106':CCF[105],'CCF_107':CCF[106],
                              'CCF_108':CCF[107],'CCF_109':CCF[108],'CCF_110':CCF[109],'CCF_111':CCF[110],'CCF_112':CCF[111],'CCF_113':CCF[112],'CCF_114':CCF[113],
                              'CCF_115':CCF[114],'CCF_116':CCF[115],'CCF_117':CCF[116],'CCF_118':CCF[117],'CCF_119':CCF[118],'CCF_120':CCF[119],
                              'CCF_121':CCF[120],'CCF_122':CCF[121],'CCF_123':CCF[122],'CCF_124':CCF[123],'CCF_125':CCF[124],'CCF_126':CCF[125],'CCF_127':CCF[126],
                              'CCF_128':CCF[127],'CCF_129':CCF[128],'CCF_130':CCF[129],'CCF_131':CCF[130],'CCF_132':CCF[131],'CCF_133':CCF[132],
                              'CCF_134':CCF[133],'CCF_135':CCF[134],'CCF_136':CCF[135],'CCF_137':CCF[136],'CCF_138':CCF[137],'CCF_139':CCF[138],'CCF_140':CCF[139],
                              'CCF_141':CCF[140],'CCF_142':CCF[141],'CCF_143':CCF[142],'CCF_144':CCF[143],'CCF_145':CCF[144],'CCF_146':CCF[145],
                              'CCF_147':CCF[146],'CCF_148':CCF[147],'CCF_149':CCF[148],'CCF_150':CCF[149],'CCF_151':CCF[150],'CCF_152':CCF[151],'CCF_153':CCF[152],
                              'CCF_154':CCF[153],'CCF_155':CCF[154],'CCF_156':CCF[155],'CCF_157':CCF[156],'CCF_158':CCF[157],'CCF_159':CCF[158],
                              'CCF_160':CCF[159],'CCF_161':CCF[160],'CCF_162':CCF[161],'CCF_163':CCF[162],'CCF_164':CCF[163],'CCF_165':CCF[164],
                              'CCF_166':CCF[165],'CCF_167':CCF[166],'CCF_168':CCF[167],'CCF_169':CCF[168],'CCF_170':CCF[169],'CCF_171':CCF[170],'CCF_172':CCF[171],
                              'CCF_173':CCF[172],'CCF_174':CCF[173],'CCF_175':CCF[174],'CCF_176':CCF[175],'CCF_177':CCF[176],'CCF_178':CCF[177],
                              'CCF_179':CCF[178],'CCF_180':CCF[179],'CCF_181':CCF[180],'CCF_182':CCF[181],'CCF_183':CCF[182],'CCF_184':CCF[183],'CCF_185':CCF[184],
                              'CCF_186':CCF[185],'CCF_187':CCF[186],'CCF_188':CCF[187],'CCF_189':CCF[188],'CCF_190':CCF[189],'CCF_191':CCF[190],
                              'CCF_192':CCF[191],'CCF_193':CCF[192],'CCF_194':CCF[193],'CCF_195':CCF[194],'CCF_196':CCF[195],'CCF_197':CCF[196],
                              'CCF_198':CCF[197],'CCF_199':CCF[198],'CCF_200':CCF[199],'CCF_201':CCF[200],'CCF_202':CCF[201],'CCF_203':CCF[202],
                              'CCF_204':CCF[203],'CCF_205':CCF[204],'CCF_206':CCF[205],'CCF_207':CCF[206],'CCF_208':CCF[207],'CCF_209':CCF[208],
                              'CCF_210':CCF[209],'CCF_211':CCF[210],'CCF_212':CCF[211],'CCF_213':CCF[212],'CCF_214':CCF[213],'CCF_215':CCF[214],
                              'CCF_216':CCF[215],'CCF_217':CCF[216],'CCF_218':CCF[217],'CCF_219':CCF[218],'CCF_220':CCF[219],'CCF_221':CCF[220],
                              'CCF_222':CCF[221],'CCF_223':CCF[222],'CCF_224':CCF[223],'CCF_225':CCF[224],'CCF_226':CCF[225],'CCF_227':CCF[226],
                              'CCF_228':CCF[227],'CCF_229':CCF[228],'CCF_230':CCF[229],'CCF_231':CCF[230],'CCF_232':CCF[231],'CCF_233':CCF[232],
                              'CCF_234':CCF[233],'CCF_235':CCF[234],'CCF_236':CCF[235],'CCF_237':CCF[236],'CCF_238':CCF[237],'CCF_239':CCF[238],
                              'CCF_240':CCF[239],'CCF_241':CCF[240],'CCF_242':CCF[241],'CCF_243':CCF[242],'CCF_244':CCF[243],'CCF_245':CCF[244],
                              'CCF_246':CCF[245],'CCF_247':CCF[246],'CCF_248':CCF[247],'CCF_249':CCF[248],'CCF_250':CCF[249],'CCF_251':CCF[250],
                              'CCF_252':CCF[251],'CCF_253':CCF[252],'CCF_254':CCF[253],'CCF_255':CCF[254],'CCF_256':CCF[255],'CCF_257':CCF[256],
                              'CCF_258':CCF[257],'CCF_259':CCF[258],'CCF_260':CCF[259],'CCF_261':CCF[260],'CCF_262':CCF[261],'CCF_263':CCF[262],
                              'CCF_264':CCF[263],'CCF_265':CCF[264],'CCF_266':CCF[265],'CCF_267':CCF[266],'CCF_268':CCF[267],'CCF_269':CCF[268],
                              'CCF_270':CCF[269],'CCF_271':CCF[270],'CCF_272':CCF[271],'CCF_273':CCF[272],'CCF_274':CCF[273],'CCF_275':CCF[274],
                              'CCF_276':CCF[275],'CCF_277':CCF[276],'CCF_278':CCF[277],'CCF_279':CCF[278],'CCF_280':CCF[279],'CCF_281':CCF[280],
                              'CCF_282':CCF[281],'CCF_283':CCF[282],'CCF_284':CCF[283],'CCF_285':CCF[284],'CCF_286':CCF[285],'CCF_287':CCF[286],
                              'CCF_288':CCF[287],'CCF_289':CCF[288],'CCF_290':CCF[289],'CCF_291':CCF[290],'CCF_292':CCF[291],'CCF_293':CCF[292],
                              'CCF_294':CCF[293],'CCF_295':CCF[294],'CCF_296':CCF[295],'CCF_297':CCF[296],'CCF_298':CCF[297],'CCF_299':CCF[298],
                              'CCF_300':CCF[299],'CCF_301':CCF[300],'CCF_302':CCF[301],'CCF_303':CCF[302],'CCF_304':CCF[303],'CCF_305':CCF[304],
                              'CCF_306':CCF[305],'CCF_307':CCF[306],'CCF_308':CCF[307],'CCF_309':CCF[308],'CCF_310':CCF[309],'CCF_311':CCF[310],
                              'CCF_312':CCF[311],'CCF_313':CCF[312],'CCF_314':CCF[313],'CCF_315':CCF[314],'CCF_316':CCF[315],'CCF_317':CCF[316],
                              'CCF_318':CCF[317],'CCF_319':CCF[318],'CCF_320':CCF[319],'CCF_321':CCF[320],'CCF_322':CCF[320],'CCF_323':CCF[322],
                              'CCF_324':CCF[323],'CCF_325':CCF[234],'CCF_326':CCF[325],'CCF_327':CCF[326],'CCF_328':CCF[327],'CCF_329':CCF[328],
                              'CCF_330':CCF[329],'CCF_331':CCF[330],'CCF_332':CCF[331],'CCF_333':CCF[332],'CCF_334':CCF[333],'CCF_335':CCF[334],
                              'CCF_336':CCF[335],'CCF_337':CCF[336],'CCF_338':CCF[337],'CCF_339':CCF[338],'CCF_340':CCF[339],'CCF_341':CCF[340],
                              'CCF_342':CCF[341],'CCF_343':CCF[342],'CCF_344':CCF[343],'CCF_345':CCF[344],'CCF_346':CCF[345],'CCF_347':CCF[346],
                              'CCF_348':CCF[347],'CCF_349':CCF[348],'CCF_350':CCF[349],'CCF_351':CCF[350],'CCF_352':CCF[351],'CCF_353':CCF[352],
                              'CCF_354':CCF[353],'CCF_355':CCF[354],'CCF_356':CCF[355],'CCF_357':CCF[356],'CCF_358':CCF[357],'CCF_359':CCF[358],
                              'CCF_360':CCF[359],'CCF_361':CCF[360],'CCF_362':CCF[361],'CCF_363':CCF[362],'CCF_364':CCF[363],'CCF_365':CCF[364],
                              'CCF_366':CCF[365],'CCF_367':CCF[366],'CCF_368':CCF[367],'CCF_369':CCF[368],'CCF_370':CCF[369],'CCF_371':CCF[370],
                              'CCF_372':CCF[371],'CCF_373':CCF[372],'CCF_374':CCF[373],'CCF_375':CCF[374],'CCF_376':CCF[375],'CCF_377':CCF[376],
                              'CCF_378':CCF[377],'CCF_379':CCF[378],'CCF_380':CCF[379],'CCF_381':CCF[380],'CCF_382':CCF[381],'CCF_383':CCF[382],
                              'CCF_384':CCF[383],'CCF_385':CCF[384],'CCF_386':CCF[385],'CCF_387':CCF[386],'CCF_388':CCF[387],'CCF_389':CCF[388],
                              'CCF_390':CCF[389],'CCF_391':CCF[390],'CCF_392':CCF[391],'CCF_393':CCF[392],'CCF_394':CCF[393],'CCF_395':CCF[394],
                              'CCF_396':CCF[395],'CCF_397':CCF[396],'CCF_398':CCF[397],'CCF_399':CCF[398],'CCF_400':CCF[399],'CCF_401':CCF[400]})
        except FileNotFoundError:
                print(locationID,apogeeID)
                pass
