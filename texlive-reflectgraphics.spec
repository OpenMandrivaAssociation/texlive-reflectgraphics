Name:		texlive-reflectgraphics
Version:	0.2c
Release:	1
Summary:	Techniques for reflecting graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/reflectgraphics
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro for reflecting images, in a number
of different ways, in pursuit of "more striking" graphics in a
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/reflectgraphics
%doc %{_texmfdistdir}/doc/latex/reflectgraphics
#- source
%doc %{_texmfdistdir}/source/latex/reflectgraphics

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
