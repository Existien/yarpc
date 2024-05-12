/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.2_enums_with_arrays.yml
 *   Object: EnumsWithArrays
 *   Template: qt6/service_source.j2
 */
#include "EnumsWithArraysInterfaceAdaptor.hpp"

using namespace gen::enums;

EnumsWithArraysInterfaceAdaptor::EnumsWithArraysInterfaceAdaptor(EnumsWithArraysInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

QList<$1> EnumsWithArraysInterfaceAdaptor::EnumMethod(
    QList<$1> color,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleEnumMethodCalled(_message);
    return {};
}

QList<$1> EnumsWithArraysInterfaceAdaptor::getEnumProperty() const {
    return m_iface->getEnumProperty();
}

void EnumsWithArraysInterfaceAdaptor::setEnumProperty(const QList<$1> &value ) {
    emit m_iface->propertyEnumPropertySet(value);
}

