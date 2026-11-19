DIGIT_INFERENCE_VERSION = 1.0
DIGIT_INFERENCE_LICENSE = MIT
DIGIT_INFERENCE_LICENSE_FILES = LICENSE
DIGIT_INFERENCE_SITE = $(TOPDIR)/../digit-inference
DIGIT_INFERENCE_SITE_METHOD = local

define DIGIT_INFERENCE_BUILD_CMDS
	$(TARGET_CC) $(TARGET_CFLAGS) $(TARGET_LDFLAGS) -O2 \
		-o $(@D)/digit_inference $(@D)/inference.c
endef

define DIGIT_INFERENCE_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/digit_inference \
		$(TARGET_DIR)/usr/bin/digit_inference
endef

$(eval $(generic-package))
