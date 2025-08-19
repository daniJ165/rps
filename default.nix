{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation rec {
  
  pname = "rps";
  version = "0.1.0";

  src = ./.;

  buildInputs = [
    pkgs.python3
    ];

    installPhase = ''
      mkdir -p $out/bin
      cp $src/rock_paper_scissors.py $out/bin/rps
      chmod +x $out/bin/rps
      '';
}
