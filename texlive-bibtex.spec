%global tl_name bibtex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.99e
Release:	%{tl_revision}.1
Summary:	Process bibliographies (bib files) for LaTeX or other formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/base
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bibtex.bin)
Requires:	texlive(kpathsea)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BibTeX allows the user to store his citation data in generic form, while
printing citations in a document in the form specified by a BibTeX
style, to be specified in the document itself (one often needs a LaTeX
citation-style package, such as natbib, as well). BibTeX knows nothing
about Unicode sorting algorithms or scripts, although it will pass on
whatever bytes it reads. Its descendant bibtexu does support Unicode,
via the ICU library. The older alternative bibtex8 supports 8-bit
character sets. Another Unicode-aware alternative is the (independently
developed) biber program, used with the BibLaTeX package to typeset its
output.

