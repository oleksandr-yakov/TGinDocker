#!/bin/bash

spinner=( Ooooo oOooo ooOoo oooOo ooooO oooOo ooOoo oOooo);
 

count(){
  spin &
  pid=$!
  sleep 1
  echo " -> Starting collapse the TgBot project"
  docker stop $(docker ps -aqf name=tgbot) 
  docker rmi -f  tgbot_img:v1
  sleep 1
  echo " -> Finished collapse the TgBot project" 
  kill $pid  
}
 
spin(){
  while [ 1 ]
  do 
    for i in ${spinner[@]}; 
    do 
      echo -ne "\r$i ";
      sleep 0.2;
    done;
  done
}
 
count
