package main

func searchClient(clients map[*CLientTemp]bool, client *CLientTemp) bool {

	for clientfor := range clients {
		if clientfor == client {
			return true
		}
	}
	return false

}
