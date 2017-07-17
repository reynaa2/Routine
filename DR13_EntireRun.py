import numpy as np
import apogee.tools.read as apread
import csv

dr13Apo = np.loadtxt('/Volumes/coveydata/APOGEE_Spectra/APOGEE2_DR13/master_apStarList_DR13.lis',skiprows=2,usecols=[3],dtype=str)
dr13Loc = np.loadtxt('/Volumes/coveydata/APOGEE_Spectra/APOGEE2_DR13/master_apStarList_DR13.lis',skiprows=2,usecols=[4],dtype=str)
path = np.loadtxt('/Volumes/coveydata/APOGEE_Spectra/APOGEE2_DR13/master_apStarList_DR13.lis',dtype = str, skiprows=2, usecols=[5]) 
newPath = [s.strip('b') for s in path]

dr13apo = []
dr13loc = []
for i in range(len(dr13Loc)):
    b = dr13Apo[i][2:-1]
    c = dr13Loc[i][2:-1]
    dr13apo.append(b)
    dr13loc.append(c)

apogeeIDs = []
locationIDs = []
for j in range(len(dr13loc)):
    if len(newPath[j]) != 36:
        apogeeIDs.append(dr13apo[j])
        locationIDs.append(dr13loc[j])
print(locationIDs[0],apogeeIDs[0])

with open('DR13_Star_Results.csv','w') as output:
    
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

    for i in range(len(locationIDs)):
            locationID = locationIDs[i]
            apogeeID = apogeeIDs[i]

            if locationID != 1:
                header = apread.apStar(locationID, apogeeID, ext=0, header=True)
                Data = apread.apStar(locationID, apogeeID, ext=9, header=False)
                nvisits = header[1]['NVISITS']

                for visit in range(0, nvisits):
                    snr = header[1]['SNRVIS'+str(visit+1)]
                    if (nvisits != 1):
                        CCF = Data['CCF'][0][2+ visit]
                    else:
                        CCF = Data['CCF'][0]
                    writer.writerow({'Location_ID': locationID, 'Apogee_ID':apogeeID, 'SNR':snr, 'CCF_1':CCF[j],'CCF_2':CCF[j+1],'CCF_3':CCF[j+2],
                  'CCF_4':CCF[j+3],'CCF_5':CCF[j+4],'CCF_6':CCF[j+5],'CCF_7':CCF[j+6],'CCF_8':CCF[j+7],'CCF_9':CCF[j+8],'CCF_10':CCF[j+9],
                  'CCF_11':CCF[j+10],'CCF_12':CCF[j+11],'CCF_13':CCF[j+12],'CCF_14':CCF[j+13],'CCF_15':CCF[j+14],'CCF_16':CCF[j+15],'CCF_17':CCF[j+16],
                  'CCF_18':CCF[j+17],'CCF_19':CCF[j+18],'CCF_20':CCF[j+19],'CCF_21':CCF[j+20],'CCF_22':CCF[j+21],'CCF_23':CCF[j+22],'CCF_24':CCF[j+23],
                  'CCF_25':CCF[j+24],'CCF_26':CCF[j+25],'CCF_27':CCF[j+26],'CCF_28':CCF[j+27],'CCF_29':CCF[j+28],'CCF_30':CCF[j+29],'CCF_31':CCF[j+30],
                  'CCF_32':CCF[j+31],'CCF_33':CCF[j+32],'CCF_34':CCF[j+33],'CCF_35':CCF[j+34],'CCF_36':CCF[j+35],'CCF_37':CCF[j+36],'CCF_38':CCF[j+37],
                  'CCF_39':CCF[j+38],'CCF_40':CCF[j+39],'CCF_41':CCF[j+40],'CCF_42':CCF[j+41],'CCF_43':CCF[j+42],'CCF_44':CCF[j+43],'CCF_45':CCF[j+44],
                  'CCF_46':CCF[j+45],'CCF_47':CCF[j+46],'CCF_48':CCF[j+47],'CCF_49':CCF[j+48],'CCF_50':CCF[j+49],'CCF_51':CCF[j+50],'CCF_52':CCF[j+51],
                  'CCF_53':CCF[j+52],'CCF_54':CCF[j+53],'CCF_55':CCF[j+54],'CCF_56':CCF[j+55],'CCF_57':CCF[j+56],'CCF_58':CCF[j+57],'CCF_59':CCF[j+58],
                  'CCF_60':CCF[j+59],'CCF_61':CCF[j+60],'CCF_62':CCF[j+61],'CCF_63':CCF[j+62],'CCF_64':CCF[j+63],'CCF_65':CCF[j+64],'CCF_66':CCF[j+65],
                  'CCF_67':CCF[j+66],'CCF_68':CCF[j+67],'CCF_69':CCF[j+68],'CCF_70':CCF[j+69],'CCF_71':CCF[j+70],'CCF_72':CCF[j+71],'CCF_73':CCF[j+72],
                  'CCF_74':CCF[j+73],'CCF_75':CCF[j+74],'CCF_76':CCF[j+75],'CCF_77':CCF[j+76],'CCF_78':CCF[j+77],'CCF_79':CCF[j+78],'CCF_80':CCF[j+79],
                  'CCF_81':CCF[j+80],'CCF_82':CCF[j+81],'CCF_83':CCF[j+82],'CCF_84':CCF[j+83],'CCF_85':CCF[j+84],'CCF_86':CCF[j+85],'CCF_87':CCF[j+86],
                  'CCF_88':CCF[j+87],'CCF_89':CCF[j+88],'CCF_90':CCF[j+89],'CCF_91':CCF[j+90],'CCF_92':CCF[j+91],'CCF_93':CCF[j+92],'CCF_94':CCF[j+93],
                  'CCF_95':CCF[j+94],'CCF_96':CCF[j+95],'CCF_97':CCF[j+96],'CCF_98':CCF[j+97],'CCF_99':CCF[j+98],'CCF_100':CCF[j+99],'CCF_101':CCF[j+100],
                  'CCF_102':CCF[j+101],'CCF_103':CCF[j+102],'CCF_104':CCF[j+103],'CCF_105':CCF[j+104],'CCF_106':CCF[j+105],'CCF_107':CCF[j+106],
                  'CCF_108':CCF[j+107],'CCF_109':CCF[j+108],'CCF_110':CCF[j+109],'CCF_111':CCF[j+110],'CCF_112':CCF[j+111],'CCF_113':CCF[j+112],'CCF_114':CCF[j+113],
                  'CCF_115':CCF[j+114],'CCF_116':CCF[j+115],'CCF_117':CCF[j+116],'CCF_118':CCF[j+117],'CCF_119':CCF[j+118],'CCF_120':CCF[j+119],
                  'CCF_121':CCF[j+120],'CCF_122':CCF[j+121],'CCF_123':CCF[j+122],'CCF_124':CCF[j+123],'CCF_125':CCF[j+124],'CCF_126':CCF[j+125],'CCF_127':CCF[j+126],
                  'CCF_128':CCF[j+127],'CCF_129':CCF[j+128],'CCF_130':CCF[j+129],'CCF_131':CCF[j+130],'CCF_132':CCF[j+131],'CCF_133':CCF[j+132],
                  'CCF_134':CCF[j+133],'CCF_135':CCF[j+134],'CCF_136':CCF[j+135],'CCF_137':CCF[j+136],'CCF_138':CCF[j+137],'CCF_139':CCF[j+138],'CCF_140':CCF[j+139],
                  'CCF_141':CCF[j+140],'CCF_142':CCF[j+141],'CCF_143':CCF[j+142],'CCF_144':CCF[j+143],'CCF_145':CCF[j+144],'CCF_146':CCF[j+145],
                  'CCF_147':CCF[j+146],'CCF_148':CCF[j+147],'CCF_149':CCF[j+148],'CCF_150':CCF[j+149],'CCF_151':CCF[j+150],'CCF_152':CCF[j+151],'CCF_153':CCF[j+152],
                  'CCF_154':CCF[j+153],'CCF_155':CCF[j+154],'CCF_156':CCF[j+155],'CCF_157':CCF[j+156],'CCF_158':CCF[j+157],'CCF_159':CCF[j+158],
                  'CCF_160':CCF[j+159],'CCF_161':CCF[j+160],'CCF_162':CCF[j+161],'CCF_163':CCF[j+162],'CCF_164':CCF[j+163],'CCF_165':CCF[j+164],
                  'CCF_166':CCF[j+165],'CCF_167':CCF[j+166],'CCF_168':CCF[j+167],'CCF_169':CCF[j+168],'CCF_170':CCF[j+169],'CCF_171':CCF[j+170],'CCF_172':CCF[j+171],
                  'CCF_173':CCF[j+172],'CCF_174':CCF[j+173],'CCF_175':CCF[j+174],'CCF_176':CCF[j+175],'CCF_177':CCF[j+176],'CCF_178':CCF[j+177],
                  'CCF_179':CCF[j+178],'CCF_180':CCF[j+179],'CCF_181':CCF[j+180],'CCF_182':CCF[j+181],'CCF_183':CCF[j+182],'CCF_184':CCF[j+183],'CCF_185':CCF[j+184],
                  'CCF_186':CCF[j+185],'CCF_187':CCF[j+186],'CCF_188':CCF[j+187],'CCF_189':CCF[j+188],'CCF_190':CCF[j+189],'CCF_191':CCF[j+190],
                  'CCF_192':CCF[j+191],'CCF_193':CCF[j+192],'CCF_194':CCF[j+193],'CCF_195':CCF[j+194],'CCF_196':CCF[j+195],'CCF_197':CCF[j+196],
                  'CCF_198':CCF[j+197],'CCF_199':CCF[j+198],'CCF_200':CCF[j+199],'CCF_201':CCF[j+200],'CCF_202':CCF[j+201],'CCF_203':CCF[j+202],
                  'CCF_204':CCF[j+203],'CCF_205':CCF[j+204],'CCF_206':CCF[j+205],'CCF_207':CCF[j+206],'CCF_208':CCF[j+207],'CCF_209':CCF[j+208],
                  'CCF_210':CCF[j+209],'CCF_211':CCF[j+210],'CCF_212':CCF[j+211],'CCF_213':CCF[j+212],'CCF_214':CCF[j+213],'CCF_215':CCF[j+214],
                  'CCF_216':CCF[j+215],'CCF_217':CCF[j+216],'CCF_218':CCF[j+217],'CCF_219':CCF[j+218],'CCF_220':CCF[j+219],'CCF_221':CCF[j+220],
                  'CCF_222':CCF[j+221],'CCF_223':CCF[j+222],'CCF_224':CCF[j+223],'CCF_225':CCF[j+224],'CCF_226':CCF[j+225],'CCF_227':CCF[j+226],
                  'CCF_228':CCF[j+227],'CCF_229':CCF[j+228],'CCF_230':CCF[j+229],'CCF_231':CCF[j+230],'CCF_232':CCF[j+231],'CCF_233':CCF[j+232],
                  'CCF_234':CCF[j+233],'CCF_235':CCF[j+234],'CCF_236':CCF[j+235],'CCF_237':CCF[j+236],'CCF_238':CCF[j+237],'CCF_239':CCF[j+238],
                  'CCF_240':CCF[j+239],'CCF_241':CCF[j+240],'CCF_242':CCF[j+241],'CCF_243':CCF[j+242],'CCF_244':CCF[j+243],'CCF_245':CCF[j+244],
                  'CCF_246':CCF[j+245],'CCF_247':CCF[j+246],'CCF_248':CCF[j+247],'CCF_249':CCF[j+248],'CCF_250':CCF[j+249],'CCF_251':CCF[j+250],
                  'CCF_252':CCF[j+251],'CCF_253':CCF[j+252],'CCF_254':CCF[j+253],'CCF_255':CCF[j+254],'CCF_256':CCF[j+255],'CCF_257':CCF[j+256],
                  'CCF_258':CCF[j+257],'CCF_259':CCF[j+258],'CCF_260':CCF[j+259],'CCF_261':CCF[j+260],'CCF_262':CCF[j+261],'CCF_263':CCF[j+262],
                  'CCF_264':CCF[j+263],'CCF_265':CCF[j+264],'CCF_266':CCF[j+265],'CCF_267':CCF[j+266],'CCF_268':CCF[j+267],'CCF_269':CCF[j+268],
                  'CCF_270':CCF[j+269],'CCF_271':CCF[j+270],'CCF_272':CCF[j+271],'CCF_273':CCF[j+272],'CCF_274':CCF[j+273],'CCF_275':CCF[j+274],
                  'CCF_276':CCF[j+275],'CCF_277':CCF[j+276],'CCF_278':CCF[j+277],'CCF_279':CCF[j+278],'CCF_280':CCF[j+279],'CCF_281':CCF[j+280],
                  'CCF_282':CCF[j+281],'CCF_283':CCF[j+282],'CCF_284':CCF[j+283],'CCF_285':CCF[j+284],'CCF_286':CCF[j+285],'CCF_287':CCF[j+286],
                  'CCF_288':CCF[j+287],'CCF_289':CCF[j+288],'CCF_290':CCF[j+289],'CCF_291':CCF[j+290],'CCF_292':CCF[j+291],'CCF_293':CCF[j+292],
                  'CCF_294':CCF[j+293],'CCF_295':CCF[j+294],'CCF_296':CCF[j+295],'CCF_297':CCF[j+296],'CCF_298':CCF[j+297],'CCF_299':CCF[j+298],
                  'CCF_300':CCF[j+299],'CCF_301':CCF[j+300],'CCF_302':CCF[j+301],'CCF_303':CCF[j+302],'CCF_304':CCF[j+303],'CCF_305':CCF[j+304],
                  'CCF_306':CCF[j+305],'CCF_307':CCF[j+306],'CCF_308':CCF[j+307],'CCF_309':CCF[j+308],'CCF_310':CCF[j+309],'CCF_311':CCF[j+310],
                  'CCF_312':CCF[j+311],'CCF_313':CCF[j+312],'CCF_314':CCF[j+313],'CCF_315':CCF[j+314],'CCF_316':CCF[j+315],'CCF_317':CCF[j+316],
                  'CCF_318':CCF[j+317],'CCF_319':CCF[j+318],'CCF_320':CCF[j+319],'CCF_321':CCF[j+320],'CCF_322':CCF[j+320],'CCF_323':CCF[j+322],
                  'CCF_324':CCF[j+323],'CCF_325':CCF[j+234],'CCF_326':CCF[j+325],'CCF_327':CCF[j+326],'CCF_328':CCF[j+327],'CCF_329':CCF[j+328],
                  'CCF_330':CCF[j+329],'CCF_331':CCF[j+330],'CCF_332':CCF[j+331],'CCF_333':CCF[j+332],'CCF_334':CCF[j+333],'CCF_335':CCF[j+334],
                  'CCF_336':CCF[j+335],'CCF_337':CCF[j+336],'CCF_338':CCF[j+337],'CCF_339':CCF[j+338],'CCF_340':CCF[j+339],'CCF_341':CCF[j+340],
                  'CCF_342':CCF[j+341],'CCF_343':CCF[j+342],'CCF_344':CCF[j+343],'CCF_345':CCF[j+344],'CCF_346':CCF[j+345],'CCF_347':CCF[j+346],
                  'CCF_348':CCF[j+347],'CCF_349':CCF[j+348],'CCF_350':CCF[j+349],'CCF_351':CCF[j+350],'CCF_352':CCF[j+351],'CCF_353':CCF[j+352],
                  'CCF_354':CCF[j+353],'CCF_355':CCF[j+354],'CCF_356':CCF[j+355],'CCF_357':CCF[j+356],'CCF_358':CCF[j+357],'CCF_359':CCF[j+358],
                  'CCF_360':CCF[j+359],'CCF_361':CCF[j+360],'CCF_362':CCF[j+361],'CCF_363':CCF[j+362],'CCF_364':CCF[j+363],'CCF_365':CCF[j+364],
                  'CCF_366':CCF[j+365],'CCF_367':CCF[j+366],'CCF_368':CCF[j+367],'CCF_369':CCF[j+368],'CCF_370':CCF[j+369],'CCF_371':CCF[j+370],
                  'CCF_372':CCF[j+371],'CCF_373':CCF[j+372],'CCF_374':CCF[j+373],'CCF_375':CCF[j+374],'CCF_376':CCF[j+375],'CCF_377':CCF[j+376],
                  'CCF_378':CCF[j+377],'CCF_379':CCF[j+378],'CCF_380':CCF[j+379],'CCF_381':CCF[j+380],'CCF_382':CCF[j+381],'CCF_383':CCF[j+382],
                  'CCF_384':CCF[j+383],'CCF_385':CCF[j+384],'CCF_386':CCF[j+385],'CCF_387':CCF[j+386],'CCF_388':CCF[j+387],'CCF_389':CCF[j+388],
                  'CCF_390':CCF[j+389],'CCF_391':CCF[j+390],'CCF_392':CCF[j+391],'CCF_393':CCF[j+392],'CCF_394':CCF[j+393],'CCF_395':CCF[j+394],
                  'CCF_396':CCF[j+395],'CCF_397':CCF[j+396],'CCF_398':CCF[j+397],'CCF_399':CCF[j+398],'CCF_400':CCF[j+399],'CCF_401':CCF[j+400]})
