Name:		texlive-reflectgraphics
Version:	40612
Release:	2
Summary:	Techniques for reflecting graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/reflectgraphics
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reflectgraphics.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
