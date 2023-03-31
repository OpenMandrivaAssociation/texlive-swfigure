Name:		texlive-swfigure
Version:	63255
Release:	2
Summary:	Insert large images that do not fit into a single page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/swfigure
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swfigure.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swfigure.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swfigure.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Five different display modes are defined in order to place in a
document large figures that do not fit into a single page. A
single user macro is defined to handle all five display modes.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/swfigure
%{_texmfdistdir}/tex/latex/swfigure
%doc %{_texmfdistdir}/doc/latex/swfigure

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
