%global tl_name reflectgraphics
%global tl_revision 40612

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2c
Release:	%{tl_revision}.1
Summary:	Techniques for reflecting graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/reflectgraphics
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a macro for reflecting images, in a number of
different ways, in pursuit of "more striking" graphics in a document.

