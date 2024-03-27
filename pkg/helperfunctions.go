package main

import (
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/schollz/progressbar/v3"
)

func DownloadAPK(filename string, url string) {
	req, _ := http.NewRequest("GET", url, nil)
	resp, _ := http.DefaultClient.Do(req)
	defer Check(resp.Body.Close)

	f, _ := os.OpenFile(fmt.Sprintf("./apks/%s.apk", "aethersx2", filename), os.O_CREATE|os.O_WRONLY, 0644)
	defer f.Close()

	bar := progressbar.DefaultBytes(
		resp.ContentLength,
		fmt.Sprintf("Downloading %s...", filename),
	)
	io.Copy(io.MultiWriter(f, bar), resp.Body)
}

// check checks the returned error of a function.
func Check(f func() error) {
	if err := f(); err != nil {
		fmt.Fprintf(os.Stderr, "received error: %v\n", err)
	}
}
