import apogee.tools.read as apread
import csv

with open('smallRound_Binary_Results.csv','w') as output:
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

  writer = csv.DictWrite(output,delimiter=',',fieldnames=names)
  writer.writeheader()

  for i in range(len(locationIDs)):
      locationID = locationIDs[i]
      apogeeID = apogeeIDs[i]

      if locationID != 1:
          header = apread.apStar(locationID, apogeeID, ext=0, header=True)
          Data = apread.apStar(locationID, apogeeID, ext=9, header=False)

          nvisits = header[1]['NVISITS']
          plt.figure(figsize=(10,10))

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
              'CCF_46':CCF[j+45],'CCF_47:CCF[j+46]','CCF_48':CCF[j+47],'CCF_49':CCF[j+48],'CCF_50':CCF[j+49],'CCF_51':CCF[j+50],'CCF_52':CCF[j+51],
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
              'CCF_154:CCF[j+153]','CCF_155':CCF[j+154],'CCF_156':CCF[j+155],'CCF_157':CCF[j+156],'CCF_158':CCF[j+157],'CCF_159':CCF[j+158],
              'CCF_160':CCF[j+159],'CCF_161':CCF[j+160],'CCF_162':CCF[j+161],'CCF_163':CCF[j+162],'CCF_164':CCF[j+163],'CCF_165':CCF[j+164],
              'CCF_166':CCF[j+165],'CCF_167':CCF[j+166],'CCF_168':CCF[j+167],'CCF_169':CCF[j+168],'CCF_170':CCF[j+169],'CCF_171':CCF[j+170],'CCF_172':CCF[j+171],
              'CCF_173':CCF[j+172],'CCF_174','CCF_175','CCF_176','CCF_177','CCF_178','CCF_179','CCF_180','CCF_181','CCF_182','CCF_183','CCF_184','CCF_185',
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
              'CCF_393','CCF_394','CCF_395','CCF_396','CCF_397','CCF_398','CCF_399','CCF_400','CCF_401'})
