This Code is one Simulator of Brazil Soccer Championship, in this code we have some interesting things, like the goal method, all teams have a number in dictionary, this number represent the goal chances of this team, like, see the team 'Botafogo', he have 6 chance of goal, but, chance of goal dont mean is goal, is just a chance, in function 'Simular_Jogo', the team is placed in situation of goal, and one command random with 30% of chance of goal decide it, if True = goal of team, if False = the team lose the goal.
  # The docs with all matchs
  - This code too create one docs with result of all match of the championship, this docs going to updated all times after one round, and you can see the results of this round, all rounds have they number on top her, please, after the execution, delete de docx, because I didn´t create one method of automatic delete, thx ^^
# Problems
- Of course, this code have some problems, and I can see it, but look, I really tried create one code with a minimum problem possible, now I´m going to list the problems I found in this code, if you want help me, fell free and you have my grateful ^^
- the first problem I found is the incorrect assignment of round, have teams playing two times in the round, all knows the teams can´t play two times. I didn´t create one function that checks if the team played, because is more difficulty than you think, if you write a code that verifies if the teams played, one moment you will stay with one round with just teams that played, and your code go stop work or return just some games, like, we need 10 games in all rounds, imagine your code return all 10 games, but in round 33 (just imagine kappa) dont have enouth teams for play, your code will stop working or return just some games, in test that I made, in the round 12 my code return just 8 games, because or the other teams go play 2 games for round or dont have teams enough, with this, I just want make you knows, it is difficulty, but you think you a better coder than me, fell free again ^^
- Another problems is the organization of front-end tabble, like, see the team 'America-MG', it´s going to be in top in all simulations, it happens because I didn´t make something for organization of this. Actually, I didn´t try and I dont have idea for how to make this, if you want make this for me, I would be very grateful.  // it is fixed, I did change in functions, now, the code put the labels of team after get the position of team - fixed
- Look, if you se other problem, you report for my email 'nagatofx3@hotmail.com', not so problem, you can tell me about one thing you think is good for code or one change, all things about code, if you want ask me about code, fell free too ^^^

I know, probaly the code have more problems, but I dont found. The frond-end is simple, I think in python is difficulty for beautiful front end HAHA.

# Changes I want make

- I really liked of the result of this code and I want make some changes in this, I´m gonna list some changes that I thought:
- I want to make the option after the simulator, the user can simulator the Libertadores Cup too, but for this, I need one simulation of Argentina League, because the Libertadores Cup use teams of all country of south america, I just want to put the teams of Argentina, in the moment I think to put the teams generics of other countrys, (real teams only for Brazil and Argentica)
- Another change I was think is the put one system of defense of the teams, for this I need a buff in number of goals, I think about this because some teams have good defensive stats, with it in mind, I can devolper one system of this, is just a some changes in function "Simular_Jogo", actually, I was change this, I think in final of today, this will be uptade


# Changes I made (octuber)
- In this month I did make some changes, for exemple, the exit button, I put one button in first screen for user can exit the app, actually, I made this after one friend report this for me, he talked "exit the aplication using alt + f4 is bad", this is simple function and I dont cast much time for make this HAHA
- Another change I did make is the screen of all games of the selected team, the user can go in button write "Abrir tela de Jogos", after this, one screen with buttons white all teams going to appared, User click in one team and all matchs of the selected team will appared in him screen
- In another commit I remember I talked about one system of defense of the team, I made this and now the teams have too one system of defense, I inspired of the real Brazil League and the most strong system defense of the teams are of 'Palmeiras', In real league is the team with less goals taked, actually, I try balanced the all teams, for all team have a real chance of win the League, but its not possible, we know that have stronger teams, like 'Palmeiras', 'Botafogo', 'Flamengo', 'Internacional', have too weaker teams like 'Atletico-GO', 'Vitoria', 'RB Bragantino', I referenced of the real league and is the more strongs and more weaks of the real league. But have one great point, the simulator is very similar of the real table, in this moment of I commited this the teams "Botafogo" is the first of league, if you simulate 3 times you will see the "Botafogo" will win one time, and the 'Palmeiras' and 'Flamengo' will be G4 almost ever time.
- Now I put some sytem of the count of wins of the home wins of the teams, is will appared in infromation of league also the screen of teams matchs

# explanation of the code

      def carregar_jogos(nome_arquivo="placares_jogos.txt"):
          global jogos_por_time
          jogos_por_time = {time: [] for time in times.keys()} 
          try:
              with open(nome_arquivo, "r") as arquivo:
                  for linha in arquivo:
                    partes = linha.strip().split(" ")
                      if len(partes) == 5:
                        time1, gols_time1, _, gols_time2, time2 = partes
                        gols_time1 = int(gols_time1)
                        gols_time2 = int(gols_time2)
                        jogos_por_time[time1].append(f"{time1} {gols_time1} x {gols_time2} {time2}")
                        jogos_por_time[time2].append(f"{time2} {gols_time2} x {gols_time1} {time1}")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de placares não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

