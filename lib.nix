{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = pkgs.python39Packages;
in
{
  python = pythonPackages.buildPythonPackage rec {
    pname = "wikipedia";
    version = "1.4.0";
    src = pythonPackages.fetchPypi {
      inherit pname version;
      sha256 = "db0fad1829fdd441b1852306e9856398204dc0786d2996dd2e0c8bb8e26133b2";
    };
    doCheck = false;
    propagatedBuildInputs = [ pythonPackages.lxml pythonPackages.beautifulsoup4 pythonPackages.requests ];
  };
}
