ROOT_MAKEFILE:=$(abspath $(patsubst %/, %, $(dir $(abspath $(lastword $(MAKEFILE_LIST))))))

include $(ROOT_MAKEFILE)/.env

export
export PATH := $(PATH):$(shell pwd)/$(UV_INSTALL_DIR)

$(eval UVEL := $(shell which uv && echo "true" || echo ""))
UVE = $(if ${UVEL},'uv',$(UV_INSTALL_DIR)/uv)

pres:
	$(UVE) sync --frozen --all-groups
	$(UVE) run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace presentation.ipynb
	BROWSER=chromium $(UVE) run jupyter notebook presentation.ipynb

install:
	which uv || [ -d "${UV_INSTALL_DIR}" ] || (curl -LsSf https://astral.sh/uv/install.sh | sh -s - --quiet)
	$(UVE) python install $(PYV)
	rm -rf .venv
	$(UVE) venv --python=$(PYV) --relocatable --link-mode=copy --seed
	$(UVE) pip install --upgrade pip
	$(UVE) sync --frozen

uninstall:
	$(UVE) python uninstall $(PYV)
	rm -rf .venv
	rm -rf "${UV_INSTALL_DIR}"

RAN := $(shell awk 'BEGIN{srand();printf("%d", 65536*rand())}')

activate:
	echo "source .venv/bin/activate; rm /tmp/$(RAN)" > /tmp/$(RAN)
	bash --init-file /tmp/$(RAN)