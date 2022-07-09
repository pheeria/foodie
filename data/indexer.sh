PATTERN='https://(.*)@(.*)'

RESTAURANTS="$(realpath ./restaurants.json)"

if [[ $BONSAI_URL =~ $PATTERN ]]; then
    AUTH="${BASH_REMATCH[1]}"
    HOST="https://${BASH_REMATCH[2]}/restaurants"

    curl -X PUT -u $AUTH $HOST -H "Content-Type: application/json" -d "@"
fi

    
