/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Enums
 *   Template: qt6/service_source.j2
 */
#include "EnumsInterfaceAdaptor.hpp"

using namespace gen::enums;

EnumsInterfaceAdaptor::EnumsInterfaceAdaptor(EnumsInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

int EnumsInterfaceAdaptor::EnumMethod(
    int color,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleEnumMethodCalled(_message);
    return {};
}

int EnumsInterfaceAdaptor::getEnumProperty() const {
    auto value = m_iface->getEnumProperty();
    return *reinterpret_cast<const int*>(&value);
}

void EnumsInterfaceAdaptor::setEnumProperty(const int &value ) {
    emit m_iface->propertyEnumPropertySet(*reinterpret_cast<const Color::Type*>(&value));
}

