
menu = True

#variabili soldi
soldi_totali_cigno = 1500
soldi_totali_palla_da_rugby = 1500

#affitti territorio
affitto_vicolo_corto = 2

#affitti in serie
affittoserie_vicolocorto = 4
affittoserie_vicolostretto = 8

#ciclo gioco
while menu:
    print("scegli un personaggio")
    print("-----------")
    scelta_personaggio = ["1-cigno", "2-palla da rugby"]
    for personaggio in scelta_personaggio:
        print(personaggio)
    print("-----------")
    sceltainput = input("scelta selezionata: ")

#cigno
    if sceltainput == "1":
        print("-----------")
        #azoni
        print("che azione scegli?")
        azioni = ["1-immobili","2-soldi","3-affitti" ]
        for azione in azioni:
            print(azione)
        print("-----------")
        scelta_azione = input("scelta selezionata: ")

        #immobili
        if scelta_azione == "1":

            #lista immobili
            lista_immobili = ["1-vicolo corto", "2-vicolo stretto"]
            for lista_immobile in lista_immobili:
                print(lista_immobile)
            nome_immobile = input("scelta selezionata: ")

            #vicolo corto
            if nome_immobile == "1":

                #lista azioni vicolo corto
                azioni_vicolo_corto = ["1-comprare"]
                for azione_vicolo_corto in azioni_vicolo_corto:
                    print(azione_vicolo_corto)
                scelta_azione_vicolo_corto = input("scelta selezionata: ")

                #comprare vicolo corto
                if scelta_azione_vicolo_corto == "1":
                    print("hai comprato vicolo corto, ti sono stati tolti 60 euro")
                    soldi_cigno_comprare_vicolo_corto = soldi_totali_cigno - 60
                    soldi_totali_cigno = soldi_cigno_comprare_vicolo_corto
                    print(soldi_totali_cigno)

            #vicolo stretto
            if nome_immobile == "2":

                #lista azioni vicolo stretto
                azioni_vicolo_stretto = ["1-comprare"]
                for azione_vicolo_stretto in azioni_vicolo_stretto:
                    print(azione_vicolo_stretto)
                scelta_azione_vicolo_stretto  = input("scelta selezionata: ")
                
                #comprare vicolo stretto
                if scelta_azione_vicolo_stretto == "1":
                    print("hai comprato vicolo stretto, ti sono stati tolti 60 euro")
                    soldi_cigno_comprare_vicolo_stretto = soldi_totali_cigno - 60
                    soldi_totali_cigno = soldi_cigno_comprare_vicolo_stretto
                    print(soldi_totali_cigno)

        #totale soldi di cigno
        if scelta_azione == "2":
            print(soldi_totali_cigno)

        #affitti
        if scelta_azione == "3":
            lista_affitti = ["1-affitto","2-affitto per serie completa"]
            for lista_affitto in lista_affitti:
                print(lista_affitto)
            scelta_affitti = input("scelta selezionata: ")

            #affitto
            if scelta_affitti == "1":
                lista_affitto_territori = ["1-vicolo corto"]
                for affitto_territorio in lista_affitto_territori:
                    print(affitto_territorio)
                scelta_affitto = input()
                if scelta_affitto == "1":
                    print("hai pagato l'affito, ti sono stati tolti: 2")
                    soldi_cigno_affitto_vicolo_corto = soldi_totali_cigno - affitto_vicolo_corto
                    soldi_totali_cigno = soldi_cigno_affitto_vicolo_corto
                    print(soldi_totali_cigno)

            #affitto in serie
            if scelta_affitti == "2":
                lista_affitti_in_serie = ["1-vicolo corto", "2-vicolo stretto"]
                for lista_affitto_in_serie in lista_affitti_in_serie:
                    print(lista_affitto_in_serie)
                scelta_affitto_in_serie = input()

                #affitto in serie di vicolo corto
                if scelta_affitto_in_serie == "1":
                    print("hai pagato l'affito in seire, ti sono stati tolti: 4")
                    soldi_cigno_affitto_in_serie_vicolo_corto = soldi_totali_cigno - affittoserie_vicolocorto
                    soldi_totali_cigno = soldi_cigno_affitto_vicolo_corto
                    print(soldi_totali_cigno)

                    #proprietario terreno vicolo corto
                    print("a chi devo aggiungere soldi?")
                    lista_proprietari_terreno_vicolo_corto_cigno = ["1-cigno", "2-palla da rugby"]
                    for lista_proprietario_terreno_vicolo_corto_cigno in lista_proprietari_terreno_vicolo_stretto_cigno:
                        print(lista_proprietario_terreno_vicolo_corto_cigno)
                    scelta_proprietario_terreno_vicolo_corto_cigno = input()

                    #proprietario vicolo corto cigno
                    if scelta_proprietario_terreno_vicolo_corto_cigno == "1":
                        print("sono stati aggiuunti: 4 euro a cigno")
                        soldi_aggiunti_a_cigno = soldi_totali_cigno + affittoserie_vicolocorto
                        soldi_totali_cigno = soldi_aggiunti_a_cigno
                        print(soldi_totali_cigno)

                #affitto in serie di vicolo stretto
                if scelta_affitto_in_serie == "2":
                    print("hai pagato l'affito in seire, ti sono stati tolti: 8")
                    soldi_cigno_affitto_in_serie_vicolo_stretto = soldi_totali_cigno - affittoserie_vicolostretto
                    soldi_totali_cigno = soldi_cigno_affitto_in_serie_vicolo_stretto
                    print(soldi_totali_cigno)

                    #proprietario terreno vicolo stretto
                    print("a chi devo aggiungere soldi?")
                    lista_proprietari_terreno_vicolo_stretto_cigno = ["1-cigno", "2-palla da rugby"]
                    for lista_proprietario_terreno_vicolo_stretto_cigno in lista_proprietari_terreno_vicolo_stretto_cigno:
                        print(lista_proprietario_terreno_vicolo_stretto_cigno)
                    scelta_proprietario_terreno_vicolo_stretto_cigno = input()

                    #proprietario vicolo stretto cigno
                    if scelta_proprietario_terreno_vicolo_stretto_cigno == "1":
                        print("sono stati aggiuunti: 8 euro a cigno"  )
                        soldi_aggiunti_a_cigno = soldi_totali_cigno + affittoserie_vicolostretto
                        soldi_totali_cigno = soldi_aggiunti_a_cigno
                        print(soldi_totali_cigno)
#palla da rugby
    if sceltainput == "2":
        #azoni
        azioni = ["1-immobili","2-soldi", ]
        for azione in azioni:
            print(azione)
        scelta_azione = input()
        #immobili
        if scelta_azione == "1":
            #lista immobili
            lista_immobili = ["1-vicolo corto"]
            for lista_immobile in lista_immobili:
                print(lista_immobile)
            nome_immobile = input()
            #vicolo corto
            if nome_immobile == "1":
                #lista azioni vicolo corto
                azioni_vicolo_corto = ["1-comprare"]
                for azione_vicolo_corto in azioni_vicolo_corto:
                    print(azione_vicolo_corto)
                scelta_azione_vicolo_corto = input()
                #comprare vicolo croto
                if scelta_azione_vicolo_corto == "1":
                    print("hai comprato vicolo corto, ti sono stati tolti 60 euro")
                    soldi_palla_da_rugby = soldi_totali_palla_da_rugby - 60
                    soldi_totali_palla_da_rugby = soldi_palla_da_rugby
                    print(soldi_totali_palla_da_rugby)