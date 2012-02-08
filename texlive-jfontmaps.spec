# revision 25317
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-jfontmaps
Version:	20120208
Release:	1
Summary:	TeXLive jfontmaps package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-jfontmaps.bin = %{EVRD}

%description
TeXLive jfontmaps package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/updmap-setup-kanji
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-morisawa.map
%{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji.pl
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/README
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/updmap-otf.sh

#-----------------------------------------------------------------------
%prep
%setup -c  -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji.pl updmap-setup-kanji
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
