import random

palabras ={'MoreComunes': '''go_back come_back ask_for put_on take_off 
get_back take_back give_up bring_up come_up find_out figure_out
hurry_up make_up show_up turn_on turn_off get_along think_about
think_of break_down'''.split(), 'WordsUp':'''make_up come_up_with cath_up throw_up wind_up
end_up cheer_up get_up wake_up grow_up mix_up pick_up put_up stand_up_to 
stand_somebody_up stand_up_for stay_up work_up think_up look_up_to turn_up 
break_up'''.split(), 'WordsOut': '''back_out chicken_out come_out cut_out drop_out duck_out fall_out 
fill_out find_out figure_out get_out_of give_out go_out hang_out head_out 
hear_our help_out kick_out point_out put_out'''.split()}
letrasCorrectas =''
espaciosVacios = '_'* len(palabras)

for i in range(len(palabras)):
    
    if palabras[i] in letrasCorrectas:
        
  
        espaciosVacios = espaciosVacios[:i] + palabras[i] + espaciosVacios[i+1:]

