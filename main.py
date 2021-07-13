
menu = True

#variabili soldi
soldi_totali_cigno = 1500
soldi_totali_palla_da_rugby = 1500
soldi_totali_gufo = 1500
soldi_totali_orso_peluche= 1500
soldi_totali_elefantino = 1500
soldi_totali_cartone_del_latte = 1500

#ciclo gioco
while menu:
    #scelta personaggi
    print(" ─────────────────────")
    print("|Scegli un personaggio|")
    print(" ─────────────────────")
    scelta_personaggio = ["1-Cigno", "2-Palla da rugby", "3-Gufo", "4-Orso di peluche", "5-Elefantino", "6-Cartone del latte"]
    for personaggio in scelta_personaggio:
        print(personaggio)
    print("────────────")
    sceltainput = input("scelta selezionata: ")

#cigno
    if sceltainput == "1":
        #azoni
        print()
        print(" ──────────────────")
        print("|Che azione scegli?|")
        print(" ──────────────────")
        azioni = ["1-Immobili","2-Affitti", "3-Soldi", "4-Passa Dal Via" ]
        for azione in azioni:
            print(azione)
        print("────────────")
        scelta_azione = input("scelta selezionata: ")

        #immobili
        if scelta_azione == "1":

            #lista immobili
            print()
            print(" ────────────────────")
            print("|Che immobili scegli?|")
            print(" ────────────────────")
            lista_immobili = ["1-Vicolo Corto", "2-Vicolo Stretto", "3-Bastioni Gran Sasso", "4-Viale Monterosa", "5-Viale Vesuvio", "6-Via Accademia", "7-Corso Ateneo", "8-Piazza Universitaria'", "9-Via Verdi", "10-Corso Raffaello", "11-Piazza Dante", "12-Viale Marco Polo", "13-Corso Magellano", "14-Largo Colombo", "15-Viale Costantino", "16-Viale Traiano", "17-Piazza Giulio Cesare", "18-Via Roma", "19-Corso Impero", "20-Largo Augusto", "21-Viale Dei Giardini", "22-Parco Della Vittoria", "23-Stazione Nord", "24-Stazione Ovest", "25-Stazione Sud", "26-Stazione Est", "27-Socita' Elettrica", "28-Soceta' Acqua Potabile"]
            for lista_immobile in lista_immobili:
                print(lista_immobile)
            print("────────────")
            nome_immobile = input("scelta selezionata: ")

            #vicolo corto
            if nome_immobile == "1":

                #lista azioni vicolo corto
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_vicolo_corto = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_vicolo_corto in azioni_vicolo_corto:
                    print(azione_vicolo_corto)
                print("────────────")
                scelta_azione_vicolo_corto = input("scelta selezionata: ")

                #comprare vicolo corto
                if scelta_azione_vicolo_corto == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato vicolo corto, ti sono stati tolti 60 euro")
                    comprare_vicolo_corto = soldi_totali_cigno - 60
                    soldi_totali_cigno = comprare_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa vicolo corto
                if scelta_azione_vicolo_corto == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Vicolo Corto, ti sono stati tolti 50 euro")
                    comprare_casa_vicolo_corto = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_casa_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel vicolo croto
                if scelta_azione_vicolo_corto == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Vicolo Corto, ti sono stati tolti 50 euro")
                    comprare_hotel_vicolo_corto = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_hotel_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca vicolo corto
                if scelta_azione_vicolo_corto == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Vicolo Corto, hai guadagnato 30 euro")
                    ipotecare_vicolo_corto = soldi_totali_cigno + 30
                    soldi_totali_cigno = ipotecare_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca vicolo corto
                if scelta_azione_vicolo_corto == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Vicolo Corto cancellata, ti sono stati tolti 33 euro")
                    ipoteca_cancellata_vicolo_corto = soldi_totali_cigno - 33
                    soldi_totali_cigno = ipoteca_cancellata_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                    
            #vicolo stretto
            if nome_immobile == "2":

                #lista azioni vicolo stretto
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_vicolo_stretto = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_vicolo_stretto in azioni_vicolo_stretto:
                    print(azione_vicolo_stretto)
                print("────────────")
                scelta_azione_vicolo_stretto = input("scelta selezionata: ")

                #comprare vicolo stretto
                if scelta_azione_vicolo_stretto == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato Vicolo Stretto, ti sono stati tolti 60 euro")
                    comprare_vicolo_stretto = soldi_totali_cigno - 60
                    soldi_totali_cigno = comprare_vicolo_stretto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa vicolo stretto
                if scelta_azione_vicolo_stretto == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Vicolo Stretto, ti sono stati tolti 50 euro")
                    comprare_casa_vicolo_stretto = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_casa_vicolo_stretto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel vicolo stretto
                if scelta_azione_vicolo_stretto == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Vicolo Stretto, ti sono stati tolti 50 euro")
                    comprare_hotel_vicolo_stretto = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_hotel_vicolo_stretto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca vicolo stretto
                if scelta_azione_vicolo_stretto == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Vicolo Stretto, hai guadagnato 30 euro")
                    ipotecare_vicolo_stretto = soldi_totali_cigno + 30
                    soldi_totali_cigno = ipotecare_vicolo_stretto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca vicolo stretto
                if scelta_azione_vicolo_stretto == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Vicolo Stretto cancellata, ti sono stati tolti 33 euro")
                    ipoteca_cancellata_vicolo_stretto = soldi_totali_cigno - 33
                    soldi_totali_cigno = ipoteca_cancellata_vicolo_stretto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            #bastioni gran sasso
            if nome_immobile == "3":
                 
                #lista azioni bastioni gran sasso
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_bastioni_gran_sasso = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_bastioni_gran_sasso in azioni_bastioni_gran_sasso:
                    print(azione_bastioni_gran_sasso)
                print("────────────")
                scelta_azione_bastioni_gran_sasso = input("scelta selezionata: ")

                #comprare bastioni gran sasso
                if scelta_azione_bastioni_gran_sasso == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato Bastioni Gran Sasso, ti sono stati tolti 100 euro")
                    comprare_bastioni_gran_sasso = soldi_totali_cigno - 100
                    soldi_totali_cigno = comprare_bastioni_gran_sasso
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa bastioni gran sasso
                if scelta_azione_bastioni_gran_sasso == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Bastioni Gran Sasso, ti sono stati tolti 50 euro")
                    comprare_casa_bastioni_gran_sasso = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_casa_bastioni_gran_sasso
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel bastioni gran sasso
                if scelta_azione_bastioni_gran_sasso == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Bastioni Gran Sasso, ti sono stati tolti 50 euro")
                    comprare_hotel_bastioni_gran_sasso = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_hotel_bastioni_gran_sasso
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca bastioni gran sasso
                if scelta_azione_bastioni_gran_sasso == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Bastioni Gran Sasso, hai guadagnato 50 euro")
                    ipotecare_bastioni_gran_sasso = soldi_totali_cigno + 50
                    soldi_totali_cigno = ipotecare_bastioni_gran_sasso
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca bastioni gran sasso
                if scelta_azione_bastioni_gran_sasso == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Bastioni Gran Sasso cancellata, ti sono stati tolti 55 euro")
                    ipoteca_cancellata_bastioni_gran_sasso = soldi_totali_cigno - 55
                    soldi_totali_cigno = ipoteca_cancellata_bastioni_gran_sasso
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            #viale monterosa
            if nome_immobile == "4":
                
                #lista azioni viale monterosa
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_viale_monterosa = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_viale_monterosa in azioni_viale_monterosa:
                    print(azione_viale_monterosa)
                print("────────────")
                scelta_azione_viale_monterosa = input("scelta selezionata: ")

                #comprare viale monterosa
                if scelta_azione_viale_monterosa == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato Viale Monterosa, ti sono stati tolti 100 euro")
                    comprare_viale_monterosa = soldi_totali_cigno - 100
                    soldi_totali_cigno = comprare_viale_monterosa
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa viale monterosa
                if scelta_azione_viale_monterosa == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Viale Monterosa, ti sono stati tolti 50 euro")
                    comprare_casa_viale_monterosa = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_casa_viale_monterosa
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel viale monterosa
                if scelta_azione_viale_monterosa == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Viale Monterosa, ti sono stati tolti 50 euro")
                    comprare_hotel_viale_monterosa = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_hotel_viale_monterosa
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca viale monterosa
                if scelta_azione_viale_monterosa == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Viale Monterosa, hai guadagnato 50 euro")
                    ipotecare_viale_monterosao = soldi_totali_cigno + 50
                    soldi_totali_cigno = ipotecare_viale_monterosa
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca viale monterosa
                if scelta_azione_viale_monterosa == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Viale Monterosa cancellata, ti sono stati tolti 55 euro")
                    ipoteca_cancellata_viale_monterosa = soldi_totali_cigno - 55
                    soldi_totali_cigno = ipoteca_cancellata_viale_monterosa
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            #viale vesuvio
            if nome_immobile == "5":
                if nome_immobile == "2":

                #lista azioni viale vesuvio
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_viale_vesuvio = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_viale_vesuvio in azioni_viale_vesuvio:
                    print(azione_viale_vesuvio)
                print("────────────")
                scelta_azione_viale_vesuvio = input("scelta selezionata: ")

                #comprare viale vesuvio
                if scelta_azione_viale_vesuvio == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato Viale Vesuvio, ti sono stati tolti 120 euro")
                    comprare_viale_vesuvio = soldi_totali_cigno - 120
                    soldi_totali_cigno = comprare_viale_vesuvio
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa viale vesuvio
                if scelta_azione_viale_vesuvio == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Viale Vesuvio, ti sono stati tolti 50 euro")
                    comprare_casa_viale_vesuvio = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_casa_viale_vesuvio
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel viale vesuvio
                if scelta_azione_viale_vesuvio == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Viale Vesuvio, ti sono stati tolti 50 euro")
                    comprare_hotel_viale_vesuvio = soldi_totali_cigno - 50
                    soldi_totali_cigno = comprare_hotel_viale_vesuvio
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca viale vesuvio
                if scelta_azione_viale_vesuvio == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Viale Vesuvio, hai guadagnato 60 euro")
                    ipotecare_viale_vesuvio = soldi_totali_cigno + 60
                    soldi_totali_cigno = ipotecare_viale_vesuvio
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca viale vesuvio
                if scelta_azione_viale_vesuvio == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Viale Vesuvio cancellata, ti sono stati tolti 66 euro")
                    ipoteca_cancellata_viale_vesuvio = soldi_totali_cigno - 66
                    soldi_totali_cigno = ipoteca_cancellata_viale_vesuvio
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            #via accademia
            if nome_immobile == "6":

                #lista via accademia
                print()
                print(" ───────────────")
                print("|Cosa vuoi fare?|")
                print(" ───────────────")
                azioni_via_accademia = ["1-Comprare territorio", "2-Comprare casa", "3-Comprare hotel", "4-ipoteca", "5-Cancella ipoteca"]
                for azione_via_accademia in azioni_via_accademia:
                    print(azione_via_accademia)
                print("────────────")
                scelta_azione_via_accademia = input("scelta selezionata: ")

                #comprare via accademia
                if scelta_azione_via_accademia == "1":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato Via Accademia, ti sono stati tolti 140 euro")
                    comprare_via_accademia = soldi_totali_cigno - 140
                    soldi_totali_cigno = comprare_via_accademia
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #comprare casa via accademia
                if scelta_azione_via_accademia == "2":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato una casa a Via Accademia, ti sono stati tolti 100 euro")
                    comprare_casa_via_accademia = soldi_totali_cigno - 100
                    soldi_totali_cigno = comprare_casa_via_accademia
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #comprare hotel via accademia
                if scelta_azione_via_accademia == "3":
                    print()
                    print(" ─────────")
                    print("|Comprato!|")
                    print(" ─────────")
                    print("Hai comprato un Hotel a Via Accademia, ti sono stati tolti 100 euro")
                    comprare_hotel_via_accademia = soldi_totali_cigno - 100
                    soldi_totali_cigno = comprare_hotel_via_accademia
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")
                
                #ipoteca via accademia
                if scelta_azione_via_accademia == "4":
                    print()
                    print(" ─────────")
                    print("|Ipotecato|")
                    print(" ─────────")
                    print("Hai ipotecato Via Accademia, hai guadagnato 70 euro")
                    ipotecare_via_accademia = soldi_totali_cigno + 70
                    soldi_totali_cigno = ipotecare_via_accademia
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                #cancella ipoteca via accademia
                if scelta_azione_via_accademia == "5":
                    print()
                    print(" ──────────────────")
                    print("|Ipoteca Cancellata|")
                    print(" ──────────────────")
                    print("Ipoteca di Via Accademia cancellata, ti sono stati tolti 77 euro")
                    ipoteca_cancellata_via_accademia = soldi_totali_cigno - 77
                    soldi_totali_cigno = ipoteca_cancellata_via_accademia
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            
        #tipi di affitti
        if scelta_azione == "2":
            print()
            print(" ─────────")
            print("|Affittasi|")
            print(" ─────────")
            
            lista_affitti = ["1-affitto","2-affitto per serie completa"]
            for lista_affitto in lista_affitti:
                print(lista_affitto)
            print("────────────")
            scelta_affitti = input("scelta selezionata: ")

            # territorio affitto
            if scelta_affitti == "1":
                print()
                print(" ───────")
                print("|Affitto|")
                print(" ───────")
                
                lista_affitto_territori = ["1-vicolo corto"]
                for affitto_territorio in lista_affitto_territori:
                    print(affitto_territorio)
                print("────────────")
                scelta_affitto = input()

                #affitto vicolo corto
                if scelta_affitto == "1":
                    print()
                    print(" ───────")
                    print("|Pagato!|")
                    print(" ───────")
                    print("hai pagato l'affito, ti sono stati tolti: 2 euro")
                    soldi_cigno_affitto_vicolo_corto = soldi_totali_cigno - affitto_vicolo_corto
                    soldi_totali_cigno = soldi_cigno_affitto_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

            #affitto in serie
            if scelta_affitti == "2":
                print()
                print(" ────────────────")
                print("|Affitto in serie|")
                print(" ────────────────")
                lista_affitti_in_serie = ["1-vicolo corto", "2-vicolo stretto"]
                for lista_affitto_in_serie in lista_affitti_in_serie:
                    print(lista_affitto_in_serie)
                print("────────────")
                scelta_affitto_in_serie = input()

                #affitto in serie di vicolo corto
                if scelta_affitto_in_serie == "1":
                    print()
                    print(" ──────")
                    print("|Pagato|")
                    print(" ──────")
                    print("hai pagato l'affito in seire, ti sono stati tolti: 4")
                    soldi_cigno_affitto_in_serie_vicolo_corto = soldi_totali_cigno - affittoserie_vicolocorto
                    soldi_totali_cigno = soldi_cigno_affitto_vicolo_corto
                    print("Ecco tutti i soldi che hai:")
                    print(soldi_totali_cigno)
                    print("────────────────────────────────────────────────")

                    #proprietario terreno vicolo corto
                    print()
                    print(" ────────────")
                    print("|Proprietario|")
                    print(" ────────────")
                    print("a chi devo aggiungere soldi?")
                    lista_proprietari_terreno_vicolo_corto_cigno = ["1-cigno", "2-palla da rugby"]
                    for lista_proprietario_terreno_vicolo_corto_cigno in lista_proprietari_terreno_vicolo_stretto_cigno:
                        print(lista_proprietario_terreno_vicolo_corto_cigno)
                    scelta_proprietario_terreno_vicolo_corto_cigno = input()

                    #proprietario vicolo corto cigno
                    if scelta_proprietario_terreno_vicolo_corto_cigno == "1":
                        print()
                        print(" ──────────")
                        print("|Guadagnato|")
                        print(" ──────────")
                        print("sono stati aggiunti: 4 euro a cigno")
                        soldi_aggiunti_a_cigno = soldi_totali_cigno + affittoserie_vicolocorto
                        soldi_totali_cigno = soldi_aggiunti_a_cigno
                        print("Ecco tutti i soldi che hai:")
                        print(soldi_totali_cigno)
                        print("────────────────────────────────────────────────")

                    #proprietario vicolo corto palla da rugby                    
                    if scelta_proprietario_terreno_vicolo_corto_cigno == "2":
                        print()
                        print(" ──────────")
                        print("|Guadagnato|")
                        print(" ──────────")
                        print("Sono stati aggiunti: 4 euro a palla da rugby")
                        soldi_aggiunti_a_palla_da_rugby = soldi_totali_palla_da_rugby + affittoserie_vicolocorto
                        soldi_totali_palla_da_rugby = soldi_aggiunti_a_palla_da_rugby
                        print("Ecco tutti i soldi che hai:")
                        print(soldi_totali_palla_da_rugby)
                        print("────────────────────────────────────────────────")

                #affitto in serie di vicolo stretto
                if scelta_affitto_in_serie == "2":
                    print()
                    print(" ──────")
                    print("|Pagato|")
                    print(" ──────")
                    print("hai pagato l'affito in seire, ti sono stati tolti: 8")
                    soldi_cigno_affitto_in_serie_vicolo_stretto = soldi_totali_cigno - affittoserie_vicolostretto
                    soldi_totali_cigno = soldi_cigno_affitto_in_serie_vicolo_stretto
                    print(soldi_totali_cigno)

                    #proprietario terreno vicolo stretto
                    print()
                    print(" ────────────")
                    print("|Proprietario|")
                    print(" ────────────")
                    print("a chi devo aggiungere soldi?")
                    lista_proprietari_terreno_vicolo_stretto_cigno = ["1-cigno", "2-palla da rugby"]
                    for lista_proprietario_terreno_vicolo_stretto_cigno in lista_proprietari_terreno_vicolo_stretto_cigno:
                        print(lista_proprietario_terreno_vicolo_stretto_cigno)
                    scelta_proprietario_terreno_vicolo_stretto_cigno = input()

                    #proprietario vicolo stretto cigno
                    if scelta_proprietario_terreno_vicolo_stretto_cigno == "1":
                        print()
                        print(" ──────────")
                        print("|Guadagnato|")
                        print(" ──────────")
                        print("sono stati aggiuunti: 8 euro a cigno"  )
                        soldi_aggiunti_a_cigno = soldi_totali_cigno + affittoserie_vicolostretto
                        soldi_totali_cigno = soldi_aggiunti_a_cigno
                        print(soldi_totali_cigno)
                        print("────────────────────────────────────────────────")

                    #proprietario vicolo stretto palla da rugby
                    if scelta_proprietario_terreno_vicolo_corto_cigno == "2":
                        print()
                        print(" ──────────")
                        print("|Guadagnato|")
                        print(" ──────────")
                        print("Sono stati aggiunti: 4 euro a palla da rugby")
                        soldi_aggiunti_a_palla_da_rugby = soldi_totali_palla_da_rugby + affittoserie_vicolocorto
                        soldi_totali_palla_da_rugby = soldi_aggiunti_a_palla_da_rugby
                        print("Ecco tutti i soldi che hai:")
                        print(soldi_totali_palla_da_rugby)
                        print("────────────────────────────────────────────────")
        #totale soldi di cigno
        if scelta_azione == "3":
            print()
            print(" ────────────────────")
            print("|Ecco i soldi totali|")
            print(" ────────────────────")
            print(soldi_totali_cigno)
            print("────────────────────────────────────────────────")
