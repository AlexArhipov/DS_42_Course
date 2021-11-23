curl -s -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=scientist' | jq . > hh.json
