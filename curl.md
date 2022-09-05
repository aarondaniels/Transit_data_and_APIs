# CURL for data transfer

curl is a command line tool used to transfer data to or from a server. It is designed to work without user interaction. It supports the following protocols: HTTP, HTTPS, SCP, SFTP, and FTP (Linuxize 2021). curl provides a number of functions that allow you to resume transfers, limit the bandwidth, provide proxy support, authenticate users, and much more (Linuxize 2021). In practice, you may also see curl referred to as cURL or Curl.

In this mini-lesson, you will learn the basic usage of the curl command, including how to download a file, save a file, and resume a download.

## Using curl

The syntax for the curl command is:

curl [options] [URL...]

To use the curl command, follow the steps below:

1. Open a Terminal and create a Docker container called curl_container on your machine using following command:
```
docker run --name curl_container -t -i ubuntu /bin/bash
apt update
apt install curl
```

2. In its simplest form, when invoked without any option, the curl command displays the specified resource to the standard output:

` curl example.com` 

3. To save the result of the curl command, use either the -o or -O option:
```
cd home
curl -o example.txt example.com
``` 
To view the file example.txt, run the commands below in the Terminal window.
```
ls
cat example.txt
```
Note: The uppercase -O option saves the file with its original file name:
```
curl -O https://cdn.jsdelivr.net/npm/vue/dist/vue.js
```

## Downloading Multiple Files

To download multiple files at once, you can use multiple -O options followed by the URL to the file that you want to download.

In the following example, you will download the Arch Linux and Debian ISO files:
```
curl -O http://mirrors.edge.kernel.org/archlinux/iso/2018.06.01/archlinux-2018.06.01-x86_64.iso  \
    -O https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.4.0-amd64-netinst.iso
```
## Resuming a Download

You can resume a download by using the -C - option. This is useful if your connection drops during the download of a large file; instead of starting the download from scratch, you can continue the previous download. For example, if you are downloading the Ubuntu 18.04 ISO file using the following command:
```
curl -O http://releases.ubuntu.com/18.04/ubuntu-18.04-live-server-amd64.iso
```
and suddenly your connection drops, you can resume the download with this command:
```
curl -C - -O http://releases.ubuntu.com/18.04/ubuntu-18.04-live-server-amd64.iso
```
The examples shown in this tutorial are simple, but they demonstrate the most commonly used curl options and are meant to help you understand how the curl command works.

More information is noted on [the official curl website](https://curl.se/).