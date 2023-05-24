{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python38;
  env = python.withPackages(ps: [
    ps.beautifulsoup4
    ps.requests
    ps.lxml
  ]);
in
with pkgs;
stdenv.mkDerivation {
  name = "myproject-env";
  buildInputs = [ env ];
  shellHook = ''
    export PYTHONPATH=${env}/lib/python3.8/site-packages
  '';
}

