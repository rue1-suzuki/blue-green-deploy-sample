if [ -f $1/docker-compose.yml ]; then
  docker stack deploy sample -c $1/docker-compose.yml
else
  echo $1/docker-compose.ymlが見つかりませんでした。
fi
