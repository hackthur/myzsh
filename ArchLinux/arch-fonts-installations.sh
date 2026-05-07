#!/bin/bash

set -e


downloadFonts(){
  local url="$1"

  echo -e "\n\nDownloading fonts"
  wget $url
  echo -e "\n\n Done..."
}

# Declaring fonts in a set

fonts=(
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Agave.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/CascadiaCode.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Hack.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Mononoki.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/UbuntuMono.zip"
  "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Iosevka.zip"
)

main(){
  for font in "${fonts[@]}"; do
    downloadFonts "$font"
  done
}

main
