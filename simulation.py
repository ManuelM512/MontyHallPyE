from monty import Monty

def game_dialogue(change):
    game = Monty(change)
    print("-Dime, ¿qué puerta vas a elegir?")
    print("-Elijo la puerta",game.player_choice+1)
    # Busca la primera puerta que tenga una cabra y que no sea la misma que eligió el jugador
    i = 0
    for i in range(3):
        if game.doors[i] == 0 and game.player_choice != i:  break
    print("-Entonces abro la puerta",i+1,"\n ¡Y había una cabra!\n Ahora, ¿vas a querer cambiar de puerta o mantenerte?")
    change_dialogue = "-Voy a cambiar de puerta" if game.change else "-Me mantengo"
    print(change_dialogue)
    print("-Detrás de la puerta había ...")
    game.play()
    win_dialogue = "Un auto! Felicitaciones!!" if game.win_result else "Una cabra! Mejor suerte la próxima!" 
    print(win_dialogue)

def game_sim(iteration_amount):
    game_results = {}
    game_results["True"]= [0,0]
    game_results["False"]= [0,0]
    for change in [True, False]:
        for i in range(iteration_amount):
            game = Monty(change)
            game.play()
            pos = 0 if game.win_result else 1
            game_results[str(change)][pos] = game_results[str(change)][pos]+1

    print("El jugador jugó",iteration_amount,"juegos cambiando, y luego sin cambiar.")
    print("\nLos resultados fueron:\n\n**Juegos cambiando**\nJuegos ganados:",game_results["True"][0])
    victory_probability = game_results["True"][0]/iteration_amount
    print("Juegos perdidos:",game_results["True"][1],"\nProbabilidad de victoria:",victory_probability)

    print()
    
    print("**Juegos sin cambiar**\nJuegos ganados:",game_results["False"][0])
    victory_probability = game_results["False"][0]/iteration_amount
    print("Juegos perdidos:",game_results["False"][1],"\nProbabilidad de victoria:",victory_probability)

game_sim(100000)
#game_dialogue(False)