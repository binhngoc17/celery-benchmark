package main

import (
	"github.com/go-martini/martini"
	"time"
)

func main() {
	m := martini.Classic()

	m.Get("/api", func(r render.Render) {
		time.Sleep(time.Second * 1)
		r.JSON(200, map[string]interface{}{"hello": "world"})
	})

	m.Run()

}
