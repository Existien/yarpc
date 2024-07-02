/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.1_arrays.yml
 *   Object: Arrays
 *   Template: qt6/service_source.j2
 */
#include "ArraysInterfaceAdaptor.hpp"

using namespace gen::arrays;

ArraysInterfaceAdaptor::ArraysInterfaceAdaptor(ArraysInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

QList<QList<double>> ArraysInterfaceAdaptor::ArrayMethod(
    QList<QList<uint>> numbers,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleArrayMethodCalled(_message);
    return {};
}

QList<QList<QString>> ArraysInterfaceAdaptor::getArrayProperty() const {
    return m_iface->getArrayProperty();
}

void ArraysInterfaceAdaptor::setArrayProperty(const QList<QList<QString>> &value ) {
    emit m_iface->propertyArrayPropertySet(value);
}

